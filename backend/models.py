from sqlalchemy import Column, Integer, String, Float, Text, Boolean
from database import Base

class DiagnosticCase(Base):
    __tablename__ = "diagnostic_cases"

    id = Column(Integer, primary_key=True, index=True)
    symptom = Column(Text, nullable=False)
    notes = Column(Text)
    show_output = Column(Text)
    
    # Deterministic Rule Results
    rule_gateway_mismatch = Column(Boolean, default=False)
    rule_interface_down = Column(Boolean, default=False)
    rule_missing_vlan = Column(Boolean, default=False)
    rule_missing_route = Column(Boolean, default=False)
    
    # AI Results
    ai_root_cause = Column(String)
    ai_confidence = Column(Float)
    ai_evidence = Column(Text)
    ai_osi_layer = Column(String)
    ai_next_command = Column(String)
    ai_fix_steps = Column(Text) # JSON-encoded list
    
    # Human Review
    status = Column(String, default="pending") # pending, accepted, edited, rejected
    human_correction = Column(Text, nullable=True)
