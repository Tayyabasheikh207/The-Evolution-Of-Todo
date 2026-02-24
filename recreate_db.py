"""
Simple test to initialize SQLModel metadata properly
"""
import sys
import os
sys.path.append(os.path.join(os.path.dirname(__file__), 'backend'))

from backend.src.models import user, todo  # Import models to register them
from backend.src.database.database import sync_engine
from sqlmodel import SQLModel

def recreate_db():
    print("Recreating database with proper model registration...")
    SQLModel.metadata.drop_all(bind=sync_engine)
    SQLModel.metadata.create_all(bind=sync_engine)
    print("Database recreated successfully!")

if __name__ == "__main__":
    recreate_db()