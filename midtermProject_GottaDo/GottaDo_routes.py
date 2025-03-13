from datetime import datetime, timedelta
from time import strftime
from typing import Annotated, Literal
from fastapi import APIRouter, Body, HTTPException, Path, status
from fastapi.encoders import isoformat
from GottaDo import Task, TaskRequest


task_get_router = APIRouter()
task_post_router = APIRouter()
task_delete_router = APIRouter()
task_update_router = APIRouter()


levels = ["task", "todo", "gottado"]
max_id: int = 0

all_dict: dict = {"task": [], "todo": [], "gottado": []}


# GET Operations
# Get all task types
@task_get_router.get("/all", status_code=status.HTTP_200_OK)
async def get_all() -> dict:
    return {"all_items": all_dict}


# Get tasks
@task_get_router.get("/tasks", status_code=status.HTTP_200_OK)
async def get_tasks() -> list:
    return all_dict["task"]


# Get todos
@task_get_router.get("/todos", status_code=status.HTTP_200_OK)
async def get_todos() -> list:
    return all_dict["todo"]


# Get gottados
@task_get_router.get("/gottados", status_code=status.HTTP_200_OK)
async def get_gottados() -> list:
    return all_dict["gottado"]


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
async def create_task(task: TaskRequest) -> Task:
    global max_id
    max_id += 1

    # Depending on type of task, set the expired_date (when you would need to re-evaluate its category)
    if task.level == "task":
        expired_date = task.created_date + timedelta(days=1)
    elif task.level == "todo":
        expired_date = task.created_date + timedelta(days=7)
    elif task.level == "gottado":
        expired_date = task.created_date + timedelta(days=30)

    newTask = Task(
        id=max_id,
        description=task.description,
        title=task.title,
        tags=task.tags,
        completed=task.completed,
        created_date=task.created_date,
        expired_date=expired_date,
        completed_date=task.completed_date,
        high_priority=task.high_priority,
        level=task.level,
    )
    level = newTask.level
    if level in levels:
        all_dict[level].append(newTask)
        return newTask

    raise HTTPException(
        status_code=status.HTTP_404_NOT_FOUND,
        detail=f"Task Type= {newTask.level} not found",
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
                task.description = desc
                return task

    raise HTTPException(
        status_code=status.HTTP_404_NOT_FOUND, detail=f"Item with ID={id} not found"
    )


# Update expire date (used for keeping the task within its current bucket upon expiration)
@task_update_router.patch("/expired_date/{id}", status_code=status.HTTP_202_ACCEPTED)
async def update_task_expired_date(
    id: Annotated[int, Path(ge=0, le=99999)],
    expired_date: Annotated[
        datetime,
        Body(
            description="The updated duedate, in datetime format",
            example="0044-03-15T00:00:00",
        ),
    ],
) -> Task:
    for type in levels:
        for i in range(len(all_dict[f"{type}"])):
            task = all_dict[type][i]
            if task.id == id:
                task.expired_date = expired_date
                return task

    raise HTTPException(
        status_code=status.HTTP_404_NOT_FOUND, detail=f"Item with ID={id} not found"
    )


# Update the completed date (when the boolean flips from 0 -> 1)
@task_update_router.patch("/completed_date/{id}", status_code=status.HTTP_202_ACCEPTED)
async def update_task_completed_date(id: Annotated[int, Path(ge=0, le=99999)]) -> Task:
    # Get the current time and make it the completed_date.
    completed_date = datetime.now()
    for type in levels:
        for i in range(len(all_dict[f"{type}"])):
            task = all_dict[type][i]
            if task.id == id:
                task.completed_date = completed_date
                return task

    raise HTTPException(
        status_code=status.HTTP_404_NOT_FOUND, detail=f"Item with ID={id} not found"
    )


@task_update_router.patch("/high_priority/{id}", status_code=status.HTTP_202_ACCEPTED)
async def update_task_priority(id: Annotated[int, Path(ge=0, le=99999)]) -> Task:
    for type in levels:
        for i in range(len(all_dict[f"{type}"])):
            task = all_dict[type][i]
            if task.id == id:
                if task.high_priority == True:
                    task.high_priority = False
                    return task
                else:
                    task.high_priority = True
                    return task

    raise HTTPException(
        status_code=status.HTTP_404_NOT_FOUND, detail=f"Item with ID={id} not found"
    )

@task_update_router.patch("/completed/{id}", status_code=status.HTTP_202_ACCEPTED)
async def update_task_completion(id: Annotated[int, Path(ge=0, le=99999)]) -> Task:
    for type in levels:
        for i in range(len(all_dict[f"{type}"])):
            task = all_dict[type][i]
            if task.id == id:
                if task.completed == True:
                    task.completed = False
                    return task
                else:
                    task.completed = True
                    return task

    raise HTTPException(
        status_code=status.HTTP_404_NOT_FOUND, detail=f"Item with ID={id} not found"
    )

@task_update_router.patch("/level/{id}", status_code=status.HTTP_202_ACCEPTED)
async def update_task_level(
    id: Annotated[int, Path(ge=0, le=99999)], level: Literal["task", "todo", "gottado"]
) -> Task:
    for type in levels:
        for i in range(len(all_dict[f"{type}"])):
            task = all_dict[type][i]
            if task.id == id:
                task.level = level
                all_dict[type].pop(i)
                all_dict[level].append(task)
                return task

    raise HTTPException(
        status_code=status.HTTP_404_NOT_FOUND, detail=f"Item with ID={id} not found"
    )
