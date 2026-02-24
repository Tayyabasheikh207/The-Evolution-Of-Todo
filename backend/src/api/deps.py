from fastapi import Depends, HTTPException, status, Request
from sqlmodel import Session
from jose import JWTError, jwt
from ..database.database import get_sync_session
from ..models.user import User
from ..services import auth_service
from ..config.settings import settings


async def get_current_user(
    request: Request,
    session: Session = Depends(get_sync_session)
) -> User:
    token = None
    authorization = request.headers.get("Authorization")
    if authorization and authorization.startswith("Bearer "):
        token = authorization[7:]

    if not token:
        raise HTTPException(
            status_code=status.HTTP_401_UNAUTHORIZED,
            detail="Authorization token required",
            headers={"WWW-Authenticate": "Bearer"},
        )

    credentials_exception = HTTPException(
        status_code=status.HTTP_401_UNAUTHORIZED,
        detail="Could not validate credentials",
        headers={"WWW-Authenticate": "Bearer"},
    )

    try:
        payload = jwt.decode(token, settings.SECRET_KEY, algorithms=[settings.ALGORITHM])
        user_id: str = payload.get("sub")
        if user_id is None:
            raise credentials_exception
    except JWTError:
        raise credentials_exception

    user = session.get(User, user_id)
    if user is None:
        raise credentials_exception
    return user


def get_optional_user(
    request: Request,
    session: Session = Depends(get_sync_session)
) -> User:
    """
    Get current user if authenticated, otherwise return None.
    Useful for routes that allow both authenticated and unauthenticated access.
    """
    try:
        return get_current_user(request, session)
    except HTTPException:
        return None