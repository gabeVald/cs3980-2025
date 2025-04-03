from datetime import datetime
from pydantic import BaseModel, PositiveInt


class User(BaseModel):
    id: int
    name: str = "John Doe"
    signup_ts: datetime | None
    tastes: dict[str, PositiveInt]


external_data = {
    "id": 123,
    "Name": "Tom",
    "signup_ts": "2020-09-21 12:22",
    "tastes": {"wine": 9, "cabbage": "1"},
}

user = User(**external_data)

print(user.tastes)
print(user.name)
# you can also try to put cabbage taste value to be -1.
# Then, check the console output.
