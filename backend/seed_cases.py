"""
seed_cases.py - Seeds the database with the 30 pre-loaded Cisco cases from cases.csv.
Run this ONCE: python seed_cases.py
"""
import csv, sys, os
sys.path.insert(0, os.path.dirname(__file__))
import models, database

models.Base.metadata.create_all(bind=database.engine)

db = database.SessionLocal()

# Check how many CSV-seeded cases exist already (they have source='csv')
existing = db.query(models.DiagnosticCase).filter(models.DiagnosticCase.notes == "__csv_seeded__").count()
if existing >= 30:
    print(f"Already seeded: {existing} CSV cases in DB. Skipping.")
    db.close()
    sys.exit(0)

csv_path = os.path.join(os.path.dirname(__file__), "..", "data", "cases.csv")

count = 0
with open(csv_path, encoding="utf-8") as f:
    reader = csv.DictReader(f)
    for row in reader:
        # Map CSV OSI layer abbreviations to full names
        layer_map = {
            "Layer1": "Layer 1 (Physical)",
            "Layer2": "Layer 2 (Data Link)",
            "Layer3": "Layer 3 (Network)",
            "Layer4": "Layer 4 (Transport)",
            "Layer7": "Layer 7 (Application)",
        }
        osi = layer_map.get(row.get("osi_layer", ""), row.get("osi_layer", ""))

        # Severity to confidence mapping
        sev_map = {"High": 0.92, "Medium": 0.75, "Low": 0.55}
        conf = sev_map.get(row.get("severity", "Medium"), 0.75)

        case = models.DiagnosticCase(
            symptom=row["symptom"],
            notes="__csv_seeded__",          # marker so we don't re-seed
            show_output=row.get("show_outputs", ""),
            rule_gateway_mismatch=False,
            rule_interface_down="line protocol is down" in row.get("show_outputs", ""),
            rule_missing_vlan="missing" in row.get("expected_fault", "").lower(),
            rule_missing_route="route" in row.get("expected_fault", "").lower(),
            ai_root_cause=row.get("expected_fault", ""),
            ai_confidence=conf,
            ai_evidence=row.get("show_outputs", ""),
            ai_osi_layer=osi,
            ai_next_command="show running-config",
            ai_fix_steps=row.get("expected_fault", ""),
            status="accept",                 # pre-validated lab cases = accepted
            human_correction="Pre-validated lab case"
        )
        db.add(case)
        count += 1

db.commit()
db.close()
print(f"Seeded {count} CSV cases into the database.")
