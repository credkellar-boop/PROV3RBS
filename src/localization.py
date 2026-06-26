import json
import os

def load_locale(lang_code: str = "en") -> dict:
    """Loads the appropriate language JSON file for the interface."""
    file_path = f"locales/{lang_code}.json"
    
    if not os.path.exists(file_path):
        file_path = "locales/en.json" # Fallback to English
        
    with open(file_path, 'r', encoding='utf-8') as f:
        return json.load(f)
      
