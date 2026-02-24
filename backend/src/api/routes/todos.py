from fastapi import APIRouter, Depends, HTTPException, status
from sqlmodel import Session
from typing import List
from uuid import UUID
from ...database.database import get_sync_session
from ...models.todo import Todo, TodoCreate, TodoUpdate, TodoRead
from ...models.user import User
from ..deps import get_current_user
from ...services.todo_service import (
    get_todos_for_user,
    get_todo_by_id,
    create_todo,
    update_todo,
    toggle_todo_completion,
    delete_todo
)


router = APIRouter()


@router.get("/", response_model=List[TodoRead])
async def read_todos(
    current_user: User = Depends(get_current_user),
    session: Session = Depends(get_sync_session)
):
    todos = get_todos_for_user(session, current_user.id)
    return todos


@router.post("/", response_model=TodoRead)
async def create_todo_item(
    todo: TodoCreate,
    current_user: User = Depends(get_current_user),
    session: Session = Depends(get_sync_session)
):
    db_todo = create_todo(session, todo, current_user.id)
    return db_todo


@router.get("/{todo_id}", response_model=TodoRead)
async def read_todo(
    todo_id: UUID,
    current_user: User = Depends(get_current_user),
    session: Session = Depends(get_sync_session)
):
    db_todo = get_todo_by_id(session, todo_id, current_user.id)
    if not db_todo:
        raise HTTPException(
            status_code=status.HTTP_404_NOT_FOUND,
            detail="Todo not found or does not belong to user"
        )
    return db_todo


@router.put("/{todo_id}", response_model=TodoRead)
async def update_todo_item(
    todo_id: UUID,
    todo_update: TodoUpdate,
    current_user: User = Depends(get_current_user),
    session: Session = Depends(get_sync_session)
):
    db_todo = update_todo(session, todo_id, todo_update, current_user.id)
    if not db_todo:
        raise HTTPException(
            status_code=status.HTTP_404_NOT_FOUND,
            detail="Todo not found or does not belong to user"
        )
    return db_todo


@router.patch("/{todo_id}/toggle-complete", response_model=TodoRead)
async def toggle_complete(
    todo_id: UUID,
    current_user: User = Depends(get_current_user),
    session: Session = Depends(get_sync_session)
):
    db_todo = toggle_todo_completion(session, todo_id, current_user.id)
    if not db_todo:
        raise HTTPException(
            status_code=status.HTTP_404_NOT_FOUND,
            detail="Todo not found or does not belong to user"
        )
    return db_todo


@router.delete("/{todo_id}")
async def delete_todo_item(
    todo_id: UUID,
    current_user: User = Depends(get_current_user),
    session: Session = Depends(get_sync_session)
):
    success = delete_todo(session, todo_id, current_user.id)
    if not success:
        raise HTTPException(
            status_code=status.HTTP_404_NOT_FOUND,
            detail="Todo not found or does not belong to user"
        )
    return {"message": "Todo deleted successfully"}