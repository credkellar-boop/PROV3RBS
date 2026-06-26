import sys
import os

# Append current directory to path to ensure modules are importable
sys.path.append(os.path.dirname(os.path.dirname(os.path.abspath(__file__))))

from src.database import Base, engine
from src.models import ChatLog

def initialize_database():
    print("Initializing PROV3RBS relational schema...")
    Base.metadata.create_all(bind=engine)
    print("Database tables generated successfully.")

if __name__ == "__main__":
    initialize_database()
  
