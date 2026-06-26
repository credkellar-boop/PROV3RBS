import json
import random

def get_proverb():
    with open('data/bank.json', 'r') as f:
        data = json.load(f)
        return random.choice(data)
      
