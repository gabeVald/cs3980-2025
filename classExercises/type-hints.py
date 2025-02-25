from typing import Annotated, Literal
from annotated_types import Gt
from pydantic import BaseModel


class Fruit(BaseModel):
    name: str
    color: Literal["red", "green"]
    weight: Annotated[float, Gt(0)]


f = Fruit(name="Apple", color="")
