from typing import Annotated
from fastapi import APIRouter, HTTPException, Path, status
from GottaDo import Task


todo_router = APIRouter()


all_list = [Task]
task_list = [Task]
todo_list = [Task]
gottado_list = [Task]


@todo_router.get("")
async def get_all() -> dict:
    return {"all_items": all_list}
