from datetime import datetime
from typing import Annotated
from fastapi import APIRouter, Body, HTTPException, Path, status
from GottaDo import Task


task_get_router = APIRouter()
task_post_router = APIRouter()
task_delete_router = APIRouter()
task_update_router = APIRouter()


levels = ["task", "todo", "gottado"]
all_dict: dict = {"task": [], "todo": [], "gottado": []}
task_list: list[Task] = []
todo_list: list[Task] = []
gottado_list: list[Task] = []


# GET Operations
# Get all task types
@task_get_router.get("/all", status_code=status.HTTP_200_OK)
async def get_all() -> dict:
    return {"all_items": all_dict}


# Get tasks
@task_get_router.get("/tasks", status_code=status.HTTP_200_OK)
async def get_tasks() -> dict:
    return {"items": task_list}


# Get todos
@task_get_router.get("/todos", status_code=status.HTTP_200_OK)
async def get_todos() -> dict:
    return {"items": todo_list}


# Get gottados
@task_get_router.get("/gottados", status_code=status.HTTP_200_OK)
async def get_gottados() -> dict:
    return {"items": gottado_list}


# Get completed
@task_get_router.get("/completed", status_code=status.HTTP_200_OK)
async def get_completed() -> dict:
    completed_items = []
    for type in levels:
        for i in range(len(all_dict[f"{type}"])):
            todo = all_dict[type][i]
            if todo.completed == True:
                completed_items.append(todo)

    if len(completed_items) >= 1:
        return {"items": completed_items}
    else:
        raise HTTPException(
            status_code=status.HTTP_404_NOT_FOUND, detail=f"No completed tasks"
        )


# POST
# Create a task
@task_post_router.post("/create", status_code=status.HTTP_201_CREATED)
async def create_task(task: Task) -> Task:
    level = task.level
    if level == "task":
        all_dict["task"].append(task)
        task_list.append(task)
        return task

    elif level == "todo":
        all_dict["todo"].append(task)
        todo_list.append(task)
        return task

    elif level == "gottado":
        all_dict["gottado"].append(task)
        gottado_list.append(task)
        return task

    raise HTTPException(
        status_code=status.HTTP_404_NOT_FOUND,
        detail=f"Task Type= {task.level} not found",
    )


# DELETE
# Delete by ID
@task_delete_router.delete("/{id}")
async def delete_task_by_id(id: Annotated[int, Path(ge=0, le=99999)]) -> dict:

    for type in levels:
        for i in range(len(all_dict[f"{type}"])):
            task = all_dict[type][i]
            if task.id == id:
                all_dict[type].pop(i)
                return {"msg": f"The task with ID={id} is removed"}

    raise HTTPException(
        status_code=status.HTTP_404_NOT_FOUND, detail=f"Item with ID={id} not found"
    )


# PATCH
# Update title
@task_update_router.patch("/title/{id}", status_code=status.HTTP_202_ACCEPTED)
async def update_task_title(
    id: Annotated[int, Path(ge=0, le=99999)],
    title: Annotated[str, Body(..., min_length=3, max_length=50)],
) -> Task:
    for type in levels:
        for i in range(len(all_dict[f"{type}"])):
            task = all_dict[type][i]
            if task.id == id:
                task.title = title
                return task

    raise HTTPException(
        status_code=status.HTTP_404_NOT_FOUND, detail=f"Item with ID={id} not found"
    )


# Update description
@task_update_router.patch("/desc/{id}", status_code=status.HTTP_202_ACCEPTED)
async def update_task_desc(
    id: Annotated[int, Path(ge=0, le=99999)],
    desc: Annotated[str, Body(..., min_length=0, max_length=1000000)],
) -> Task:
    for type in levels:
        for i in range(len(all_dict[f"{type}"])):
            task = all_dict[type][i]
            if task.id == id:
                task.desc = desc
                return task

    raise HTTPException(
        status_code=status.HTTP_404_NOT_FOUND, detail=f"Item with ID={id} not found"
    )

@task_update_router.patch("/due/{id}", status_code=status.HTTP_202_ACCEPTED)
async def update_task_duedate(id: Annotated[int, Path(ge=0, le=99999)], duedate: Annotated[datetime, Body(description="The updated duedate, in datetime format",example="2023-01-01T00:00:00Z")]) -> datetime:
    
