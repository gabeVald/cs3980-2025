from typing import Annotated
from fastapi import FastAPI, APIRouter, Path
from enum import Enum

from fastapi.responses import FileResponse
from fastapi.staticfiles import StaticFiles
from GottaDo_routes import task_router

app = FastAPI(Title="My todo App")

app.include_router(task_router, tags=["Tasks"], prefix="/tasks")


@app.get("/")
async def welcome() -> dict:
    """My document summary"""
    return FileResponse("./frontend/index.html")


app.mount("/", StaticFiles(directory="frontend"), name="assets")
