from typing import Annotated
from fastapi import FastAPI, APIRouter, Path
from enum import Enum
from todo_routes import todo_router

app = FastAPI(Title="My todo App")

app.include_router(todo_router, tags=["todos"], prefix="/todos")


@app.get("/")
async def welcome() -> dict:
    """My document summary"""
    return {"msg": "Hello"}


@app.get("/items")
async def get_items() -> dict:
    """My document summary"""
    return {"item_1": "book_1"}


@app.get(
    "/items/{item_id}",
    summary="Get an item",
    description="## This is the lalalalal description of the route",
)
async def get_items(
    item_id: Annotated[
        int,
        Path(title="This is the item ID, which should be an integer", ge=0, le=1000),
    ]
) -> dict:
    """My document summary"""
    if item_id == 1:
        return {"item_1": "book_1"}
    else:
        return {}


class PersonType(str, Enum):
    student = "Student"
    employee = "Employee"
    patient = "Patient"


@app.get("/persons/{person_type}")
async def get_person_with_type(person_type: PersonType) -> dict:
    """My document summary"""
    # Type checking using is
    if person_type is PersonType.student:
        return {"item_1": "book_1"}
    elif person_type is PersonType.employee:
        return {"item_2": "book_2"}
    # elif person_type is PersonType.patient:
    # return {"item_3": "book_3"}
    # Primitive value comparison using ==
    if person_type.value == "Patient":
        return {"item_1": "p1 t1"}
    else:
        return {}
