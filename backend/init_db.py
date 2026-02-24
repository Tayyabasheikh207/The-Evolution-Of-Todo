"""Script to initialize the database with required tables."""

import sys
import os
sys.path.append(os.path.join(os.path.dirname(__file__), '.'))

from sqlmodel import SQLModel
from src.database.database import sync_engine
from src.models.user import User
from src.models.todo import Todo

def create_db_and_tables():
    """Create database tables."""
    print("Creating database tables...")
    SQLModel.metadata.create_all(bind=sync_engine)
    print("Database tables created successfully!")

if __name__ == "__main__":
    create_db_and_tables()