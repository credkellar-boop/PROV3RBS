import json
import sys

def validate():
    with open('data/bank.json', 'r') as f:
        data = json.load(f)
        if len(data) != 915:
            print(f"Error: Expected 915, found {len(data)}")
            sys.exit(1)
    print("Integrity check passed.")

if __name__ == "__main__":
    validate()
  
