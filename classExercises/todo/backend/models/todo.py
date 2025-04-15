from pydantic import BaseModel

# THIS IS THE CURRENT USED FOLDER, OLD IS DEPRECATED IN PROJECT ROOT


class Todo(BaseModel):
    id: int
    title: str
    desc: str


# Used to create todos
class TodoRequest(BaseModel):
    title: str
    desc: str