from sqlmodel import SQLModel, Field, Relationship
from typing import TYPE_CHECKING, Optional
import uuid
from datetime import datetime
from pydantic import validator

if TYPE_CHECKING:
    from .user import User  # pragma: no cover


class TodoBase(SQLModel):
    content: str = Field(nullable=False, max_length=500)
    completed: bool = Field(default=False)


class Todo(TodoBase, table=True):
    id: Optional[uuid.UUID] = Field(default_factory=uuid.uuid4, primary_key=True)
    content: str = Field(nullable=False, max_length=500)
    completed: bool = Field(default=False)
    user_id: uuid.UUID = Field(foreign_key="user.id", nullable=False)
    created_at: datetime = Field(default_factory=datetime.utcnow)
    updated_at: datetime = Field(default_factory=datetime.utcnow)

    # Relationship to user (temporarily commented out due to circular import issues)
    # user: Optional["User"] = Relationship(back_populates="todos", sa_relationship_kwargs={"lazy": "select"})


class TodoCreate(TodoBase):
    content: str

    @validator('content')
    def validate_content(cls, v):
        if not v or len(v.strip()) == 0:
            raise ValueError('Content cannot be empty')
        if len(v) > 500:
            raise ValueError('Content cannot exceed 500 characters')
        return v.strip()


class TodoRead(TodoBase):
    id: uuid.UUID
    user_id: uuid.UUID
    created_at: datetime
    updated_at: datetime


class TodoUpdate(SQLModel):
    content: Optional[str] = None
    completed: Optional[bool] = None

    @validator('content')
    def validate_content(cls, v):
        if v is not None:
            if not v or len(v.strip()) == 0:
                raise ValueError('Content cannot be empty')
            if len(v) > 500:
                raise ValueError('Content cannot exceed 500 characters')
            return v.strip()
        return v