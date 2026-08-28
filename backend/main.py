from fastapi import FastAPI, Depends, HTTPException, Header
from fastapi.middleware.cors import CORSMiddleware
from sqlalchemy.orm import Session
from pydantic import BaseModel
import uvicorn
from typing import List, Optional

import models, database
from rule_checker import run_rules
from ai_engine import get_ai_diagnosis

models.Base.metadata.create_all(bind=database.engine)

# Auto-cleanup junk/random test cases from DB on startup
db_session = database.SessionLocal()
try:
    pending_cases = db_session.query(models.DiagnosticCase).filter(models.DiagnosticCase.status == "pending").all()
    deleted = 0
    for c in pending_cases:
        sym = c.symptom.strip()
        # If symptom is too short (< 10 chars) or matches common gibberish strings
        if len(sym) < 10 or sym.lower() in ["sdfds", "fddsfds", "test", "hello", "random"]:
            db_session.delete(c)
            deleted += 1
    if deleted > 0:
        db_session.commit()
        print(f"Startup DB Cleanup: Deleted {deleted} garbage test cases.")
except Exception as e:
    print("Startup cleanup error:", e)
finally:
    db_session.close()

app = FastAPI(title="NetSage AI Backend")

# Enable CORS for React frontend
app.add_middleware(
    CORSMiddleware,
    allow_origins=["*"],
    allow_credentials=True,
    allow_methods=["*"],
    allow_headers=["*"],
)

class DiagnoseRequest(BaseModel):
    symptom: str
    notes: str = ""
    show_output: str = ""

class ReviewRequest(BaseModel):
    case_id: int
    action: str # accept, edit, reject
    correction: str = ""

import re

def normalize_text(text):
    if not text:
        return ""
    return re.sub(r'[^a-zA-Z0-9]', '', text).lower()

@app.post("/api/diagnose")
def diagnose(req: DiagnoseRequest, x_gemini_api_key: Optional[str] = Header(None), db: Session = Depends(database.get_db)):
    # Normalize input symptom for lookup
    norm_symptom = normalize_text(req.symptom)
    
    # Check if this symptom matches any of the 30 pre-loaded CSV cases
    preloaded = None
    if len(norm_symptom) > 10:
        # Fetch all seeded cases
        seeded_cases = db.query(models.DiagnosticCase).filter(models.DiagnosticCase.notes == "__csv_seeded__").all()
        for sc in seeded_cases:
            if normalize_text(sc.symptom) == norm_symptom or norm_symptom in normalize_text(sc.symptom) or normalize_text(sc.symptom) in norm_symptom:
                preloaded = sc
                break
                
    if preloaded:
        # Preloaded match found! Return the saved diagnosis directly (no API call, 100% stable)
        rule_results = {
            "gateway_mismatch": preloaded.rule_gateway_mismatch,
            "interface_down": preloaded.rule_interface_down,
            "missing_vlan": preloaded.rule_missing_vlan,
            "missing_route": preloaded.rule_missing_route
        }
        
        # Parse fix_steps
        import ast
        try:
            fix_steps = ast.literal_eval(preloaded.ai_fix_steps)
        except Exception:
            fix_steps = [preloaded.ai_fix_steps] if preloaded.ai_fix_steps else []
            
        ai_result = {
            "root_cause": preloaded.ai_root_cause,
            "confidence": preloaded.ai_confidence,
            "osi_layer": preloaded.ai_osi_layer,
            "evidence": preloaded.ai_evidence,
            "next_command": preloaded.ai_next_command,
            "fix_steps": fix_steps
        }
    else:
        # 1. Run deterministic rules
        rule_results = run_rules(req.symptom, req.notes, req.show_output)
        
        # 2. Get AI structured diagnosis (Live Gemini fallback)
        ai_result = get_ai_diagnosis(req.symptom, req.notes, req.show_output, rule_results, custom_api_key=x_gemini_api_key)
    
    # 3. Save to database
    case = models.DiagnosticCase(
        symptom=req.symptom,
        notes=req.notes,
        show_output=req.show_output,
        rule_gateway_mismatch=rule_results.get("gateway_mismatch", False),
        rule_interface_down=rule_results.get("interface_down", False),
        rule_missing_vlan=rule_results.get("missing_vlan", False),
        rule_missing_route=rule_results.get("missing_route", False),
        ai_root_cause=ai_result.get("root_cause"),
        ai_confidence=ai_result.get("confidence", 0.0),
        ai_evidence=ai_result.get("evidence"),
        ai_osi_layer=ai_result.get("osi_layer"),
        ai_next_command=ai_result.get("next_command"),
        ai_fix_steps=str(ai_result.get("fix_steps", [])),
        status="pending"
    )
    db.add(case)
    db.commit()
    db.refresh(case)
    
    return {
        "case_id": case.id,
        "rule_results": rule_results,
        "ai_diagnosis": ai_result
    }

@app.post("/api/review")
def review(req: ReviewRequest, db: Session = Depends(database.get_db)):
    case = db.query(models.DiagnosticCase).filter(models.DiagnosticCase.id == req.case_id).first()
    if not case:
        raise HTTPException(status_code=404, detail="Case not found")
        
    case.status = req.action
    if req.action in ["edit", "reject"]:
        case.human_correction = req.correction
        
    db.commit()
    return {"status": "success", "case_id": case.id}

@app.get("/api/stats")
def get_stats(db: Session = Depends(database.get_db)):
    total = db.query(models.DiagnosticCase).count()
    accepted = db.query(models.DiagnosticCase).filter(models.DiagnosticCase.status == "accept").count()
    edited = db.query(models.DiagnosticCase).filter(models.DiagnosticCase.status == "edit").count()
    rejected = db.query(models.DiagnosticCase).filter(models.DiagnosticCase.status == "reject").count()
    pending = db.query(models.DiagnosticCase).filter(models.DiagnosticCase.status == "pending").count()
    
    return {
        "total": total,
        "accepted": accepted,
        "edited": edited,
        "rejected": rejected,
        "pending": pending
    }

@app.get("/api/cases")
def get_cases(db: Session = Depends(database.get_db)):
    cases = db.query(models.DiagnosticCase).order_by(models.DiagnosticCase.id.desc()).all()
    return cases

if __name__ == "__main__":
    uvicorn.run("main:app", host="0.0.0.0", port=8000, reload=True)
