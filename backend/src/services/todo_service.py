from sqlmodel import Session, select
from typing import List, Optional
from uuid import UUID
from ..models.todo import Todo, TodoCreate, TodoUpdate
from ..models.user import User


def get_todos_for_user(session: Session, user_id: UUID) -> List[Todo]:
    statement = select(Todo).where(Todo.user_id == user_id)
    return session.execute(statement).scalars().all()


def get_todo_by_id(session: Session, todo_id: UUID, user_id: UUID) -> Optional[Todo]:
    statement = select(Todo).where(Todo.id == todo_id, Todo.user_id == user_id)
    return session.execute(statement).scalar()


def create_todo(session: Session, todo_create: TodoCreate, user_id: UUID) -> Todo:
    db_todo = Todo(
        content=todo_create.content,
        completed=todo_create.completed,
        user_id=user_id
    )
    session.add(db_todo)
    session.commit()
    session.refresh(db_todo)
    return db_todo


def update_todo(session: Session, todo_id: UUID, todo_update: TodoUpdate, user_id: UUID) -> Optional[Todo]:
    db_todo = session.get(Todo, todo_id)
    if not db_todo or db_todo.user_id != user_id:
        return None

    # Update fields if provided
    update_data = todo_update.dict(exclude_unset=True)
    for field, value in update_data.items():
        setattr(db_todo, field, value)

    session.add(db_todo)
    session.commit()
    session.refresh(db_todo)
    return db_todo


def toggle_todo_completion(session: Session, todo_id: UUID, user_id: UUID) -> Optional[Todo]:
    db_todo = session.get(Todo, todo_id)
    if not db_todo or db_todo.user_id != user_id:
        return None

    db_todo.completed = not db_todo.completed
    session.add(db_todo)
    session.commit()
    session.refresh(db_todo)
    return db_todo


def delete_todo(session: Session, todo_id: UUID, user_id: UUID) -> bool:
    db_todo = session.get(Todo, todo_id)
    if not db_todo or db_todo.user_id != user_id:
        return False

    session.delete(db_todo)
    session.commit()
    return True