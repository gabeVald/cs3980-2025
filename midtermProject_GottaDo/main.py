from typing import Annotated
from fastapi import FastAPI, APIRouter, Path
from enum import Enum

from fastapi.responses import FileResponse
from fastapi.staticfiles import StaticFiles
from GottaDo_routes import (
    task_get_router,
    task_post_router,
    task_delete_router,
    task_update_router,
)

app = FastAPI(Title="GottaDo App")

app.include_router(task_get_router, tags=["GET get tasks types"], prefix="/tasks")
app.include_router(task_post_router, tags=["POST create tasks"], prefix="/tasks")
app.include_router(task_delete_router, tags=["DELETE create tasks"], prefix="/tasks")
app.include_router(task_update_router, tags=["UPDATE update tasks"], prefix="/tasks")


@app.get("/")
async def welcome() -> dict:
    """My document summary"""
    return FileResponse("./frontend/index.html")


app.mount("/", StaticFiles(directory="frontend"), name="assets")
