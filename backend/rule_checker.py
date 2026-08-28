import re

def run_rules(symptom: str, notes: str, show_output: str) -> dict:
    text = f"{symptom}\n{notes}\n{show_output}".lower()
    
    rules = {
        "gateway_mismatch": False,
        "interface_down": False,
        "missing_vlan": False,
        "missing_route": False,
        "duplicate_ip": False,
        "wrong_mask": False
    }
    
    # 1. Interface Down
    if "administratively down" in text or "line protocol is down" in text:
        rules["interface_down"] = True
        
    # 2. Duplicate IP
    if "duplicate" in text and "ip" in text:
        rules["duplicate_ip"] = True
        
    # 3. Missing Route
    if "network not in table" in text or "subnet not in table" in text or "no route" in text:
        rules["missing_route"] = True
        
    # 4. Missing VLAN
    if "vlan" in text and ("not active" in text or "does not exist" in text or "not found" in text):
        rules["missing_vlan"] = True
        
    # 5. Wrong Mask
    if "bad mask" in text or "invalid mask" in text or "overlaps with" in text:
        rules["wrong_mask"] = True
        
    # 6. Gateway Mismatch
    if "default gateway" in text and ("unreachable" in text or "not set" in text):
        rules["gateway_mismatch"] = True
        
    return rules
