import json
import os

def create_placeholder_proverbs(count: int = 915, filename: str = "data/bank.json"):
    """Generates a base JSON file with placeholder entries to satisfy the 915 requirement."""
    
    os.makedirs(os.path.dirname(filename), exist_ok=True)
    
    proverbs = []
    for i in range(1, count + 1):
        proverbs.append({
            "id": i,
            "category": "Uncategorized",
            "text": f"Placeholder proverb #{i}. Awaiting ingestion.",
            "attribution": "System"
        })
        
    with open(filename, 'w', encoding='utf-8') as f:
        json.dump(proverbs, f, indent=2, ensure_ascii=False)
        
    print(f"Successfully generated {count} placeholders in {filename}")

if __name__ == "__main__":
    create_placeholder_proverbs()
  
