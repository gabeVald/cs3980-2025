from typing import Annotated
from fastapi import APIRouter, HTTPException, Path, status
from todo import Todo


todo_router = APIRouter()

todo_list = []


@todo_router.get("")
async def get_todos() -> dict:
    return {"todos": todo_list}


@todo_router.post("", status_code=status.HTTP_201_CREATED)
async def add_todo(
    todo: Todo,
) -> (
    Todo
):  # Returning the Todo type that we created, which could be used to update the frontend
    todo_list.append(todo)
    return todo


@todo_router.get("/{id}")
async def get_todo_by_id(id: Annotated[int, Path(ge=0, le=1000)]) -> Todo:
    for todo in todo_list:
        if todo.id == id:
            return todo
    raise HTTPException(
        status_code=status.HTTP_404_NOT_FOUND, detail=f"Item with ID={id} not found"
    )  # Best way to let the client know that there is no value for the id


@todo_router.delete("/{id}")
async def delete_todo_by_id(id: Annotated[int, Path(ge=0, le=1000)]) -> dict:
    for i in range(len(todo_list)):
        todo = todo_list[i]
        if todo.id == id:
            todo_list.pop(i)
            return {"msg": f"The todo with ID={id} is removed"}

    raise HTTPException(
        status_code=status.HTTP_404_NOT_FOUND, detail=f"Item with ID={id} not found"
    )
