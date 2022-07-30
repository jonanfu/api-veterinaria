#Python
from datetime import datetime

#Pydantic
from pydantic import BaseModel
from pydantic import Field


class EstheticCreate(BaseModel):
    date: datetime = Field(...)
    hour: datetime = Field(...)
    activate_notification:bool = Field(default = False)
    price:float = Field(...)
    form_payment:str = Field(
        ...,
        min_length = 1,
        max_length = 50,
        example = 'form payment'
    )
    is_paid:bool = Field(default = False)
    patient:int = Field(...)

class Esthetic(EstheticCreate):
    id: int = Field(...)
