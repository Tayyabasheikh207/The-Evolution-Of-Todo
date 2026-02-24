from fastapi import APIRouter, Depends, HTTPException, status
from sqlmodel import Session
from typing import Dict
from ...database.database import get_sync_session
from ...models.user import User, UserCreate, UserRead
from ...services import auth_service
from ...services.user_service import create_user as create_user_service


router = APIRouter()


@router.post("/signup", response_model=UserRead)
def signup(user_create: UserCreate, session: Session = Depends(get_sync_session)):
    try:
        db_user = create_user_service(session, user_create)
        return db_user
    except ValueError as e:
        raise HTTPException(
            status_code=status.HTTP_409_CONFLICT,
            detail=str(e)
        )


@router.post("/signin")
def signin(form_data: Dict[str, str], session: Session = Depends(get_sync_session)):
    email = form_data.get("email")
    password = form_data.get("password")

    if not email or not password:
        raise HTTPException(
            status_code=status.HTTP_400_BAD_REQUEST,
            detail="Email and password are required"
        )

    user = auth_service.authenticate_user(session, email, password)
    if not user:
        raise HTTPException(
            status_code=status.HTTP_401_UNAUTHORIZED,
            detail="Incorrect email or password",
            headers={"WWW-Authenticate": "Bearer"},
        )

    access_token = auth_service.create_access_token(
        data={"sub": str(user.id)}
    )

    return {
        "success": True,
        "user": {
            "id": user.id,
            "email": user.email
        },
        "token": access_token
    }


@router.post("/signout")
def signout():
    # In a real implementation, you might want to invalidate tokens
    # For now, we'll just return a success message
    return {
        "success": True,
        "message": "Signed out successfully"
    }