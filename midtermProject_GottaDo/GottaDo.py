from datetime import datetime
from fastapi import APIRouter
from pydantic import BaseModel

levels = ["task", "todo", "gottado"]


class Task(BaseModel):
    id: int
    description: str
    title: str = "New Task"
    tags: list[str] = []
    completed: bool = False
    created_date: datetime  # When the task was initially created
    expired_date: (
        datetime  # When the task moves up to the next level (task -> todo -> gottado)
    )
    completed_date: datetime  # When the completed boolean flips from 0 -> 1
    high_priority: bool = False
    level: str = "task"
