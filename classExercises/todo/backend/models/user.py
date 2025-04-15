from beanie import Document

class User(Document):
    username: str
    email: str # user pydantic email for final project
    password: str

    class Settings:
        name = "users"
