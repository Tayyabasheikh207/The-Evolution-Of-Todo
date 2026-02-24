from sqlmodel import Session, select
from typing import Optional
from ..models.user import User, UserCreate, UserUpdate
from ..services.auth_service import get_password_hash


def get_user_by_id(session: Session, user_id: str) -> Optional[User]:
    return session.get(User, user_id)


def get_user_by_email(session: Session, email: str) -> Optional[User]:
    statement = select(User).where(User.email == email)
    return session.execute(statement).scalar()


def create_user(session: Session, user_create: UserCreate) -> User:
    # Check if user already exists
    existing_user = session.execute(select(User).where(User.email == user_create.email)).scalar()
    if existing_user:
        raise ValueError("Email already registered")

    # Create new user
    hashed_password = get_password_hash(user_create.password)
    db_user = User(
        email=user_create.email,
        password_hash=hashed_password
    )
    session.add(db_user)
    session.commit()
    session.refresh(db_user)
    return db_user


def update_user(session: Session, user_id: str, user_update: UserUpdate) -> Optional[User]:
    db_user = session.get(User, user_id)
    if not db_user:
        return None

    # Update fields if provided
    if user_update.email is not None:
        db_user.email = user_update.email

    session.add(db_user)
    session.commit()
    session.refresh(db_user)
    return db_user


def delete_user(session: Session, user_id: str) -> bool:
    db_user = session.get(User, user_id)
    if not db_user:
        return False

    session.delete(db_user)
    session.commit()
    return True