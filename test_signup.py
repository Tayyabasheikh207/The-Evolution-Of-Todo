"""
Test script to simulate the signup process and identify the error.
"""

import sys
import os
sys.path.append(os.path.join(os.path.dirname(__file__), 'backend'))

from backend.src.services.auth_service import create_user
from backend.src.models.user import UserCreate
from backend.src.database.database import get_sync_session
from sqlmodel import Session

def test_signup():
    print("Testing signup process...")

    # Create a new session
    with next(get_sync_session()) as session:
        try:
            # Create a test user with a shorter password
            user_create = UserCreate(email="test@example.com", password="pass123")

            print(f"Attempting to create user with email: {user_create.email}")

            # Try to create the user
            db_user = create_user(session, user_create)
            print(f"User created successfully: {db_user.email}")
            print(f"User ID: {db_user.id}")

        except Exception as e:
            print(f"Error occurred during signup: {str(e)}")
            import traceback
            print("Full traceback:")
            traceback.print_exc()

if __name__ == "__main__":
    test_signup()