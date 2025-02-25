from fastapi import APIRouter
from pydantic import BaseModel
from todo_routes import todo_router


class Todo(BaseModel):
    id: int
    desc: str


todo_list = []


# GET
@todo_router.get("")
async def get_todos() -> dict:
    return {"todos": todo_list}


# POST
@todo_router.post("")
async def add_todo(todo: Todo) -> dict:
    todo_list.append(todo)
    return {"msg": "todo created"}
