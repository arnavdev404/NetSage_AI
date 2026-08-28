import os
import json
import google.generativeai as genai

# Fallback Antigravity key
DEFAULT_KEY = ""  # Put your API key in environment variable GEMINI_API_KEY

def get_ai_diagnosis(symptom: str, notes: str, show_output: str, rule_results: dict, custom_api_key: str = None):
    # 1. Input validation to prevent wasting API quota on random gibberish or empty text
    clean_symptom = symptom.strip()
    if len(clean_symptom) < 8 or not any(c.isalpha() for c in clean_symptom):
        return {
            "root_cause": "Please enter a descriptive, valid network symptom (e.g., 'PC has IP but cannot reach server').",
            "confidence": 0.0,
            "osi_layer": "Unknown",
            "evidence": "Invalid or too short symptom input.",
            "next_command": "None",
            "fix_steps": ["Enter a valid symptom description", "Provide relevant configuration or notes"]
        }

    # Determine which API key and model to use
    api_key = custom_api_key.strip() if (custom_api_key and custom_api_key.strip()) else None
    
    if api_key:
        # Standard Google AI Studio key (e.g. AIzaSy...)
        client_key = api_key
        model_name = "gemini-1.5-flash"  # Standard free tier model
    else:
        # System fallback key
        client_key = os.environ.get("GEMINI_API_KEY", DEFAULT_KEY)
        model_name = "gemini-3.5-flash"  # Designated proxy model name
        
    prompt = f"""
    You are a Cisco network troubleshooting expert.
    
    SYMPTOM:
    {symptom}
    
    NOTES:
    {notes}
    
    SHOW OUTPUT:
    {show_output}
    
    RULE CHECKER RESULTS (Deterministic Checks):
    {json.dumps(rule_results, indent=2)}
    
    Analyze the problem and incorporate the deterministic rule check results into your reasoning.
    Provide your diagnosis STRICTLY in the following JSON schema:
    {{
      "root_cause": "A single sentence explaining the fault",
      "confidence": 0.0 to 1.0,
      "osi_layer": "Layer 1 - Physical, etc",
      "evidence": "Specific evidence from the output",
      "next_command": "Command to run next",
      "fix_steps": ["step 1", "step 2", "step 3"]
    }}
    """
    
    try:
        # Configure dynamically for this call
        genai.configure(api_key=client_key)
        model = genai.GenerativeModel(model_name, generation_config={"response_mime_type": "application/json"})
        response = model.generate_content(prompt)
        return json.loads(response.text)
    except Exception as e:
        err_msg = str(e)
        # Handle 429 Quota limits gracefully
        if "429" in err_msg or "quota" in err_msg.lower() or "limit" in err_msg.lower():
            if api_key:
                root_cause = "Your custom Gemini API Key has reached its rate limit. Please wait 15 seconds and try again."
            else:
                root_cause = "The NetSage shared AI Engine is currently busy (Daily Free Quota Limit Reached). To bypass this, please paste your own free Gemini API key in the configuration field above."
        else:
            root_cause = f"AI Error: {err_msg}"
            
        return {
            "root_cause": root_cause,
            "confidence": 0.0,
            "osi_layer": "Unknown",
            "evidence": "API request failed or limit reached.",
            "next_command": "None",
            "fix_steps": []
        }
