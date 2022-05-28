#Python
from datetime import datetime

#Pydantic
from pydantic import BaseModel
from pydantic import Field


class EstheticCreate(BaseModel):
    date: Optional[date] = Field(default = datetime.now)
    hour: Optional[date] = Field(default = datetime.now)
    activate_notification:bool = Field(default = False)
    price:float = Field(...)
    form_payment:str = Field(
        ...,
        min_length = 1,
        max_length = 50,
        example = 'form payment'
    )
    is_paid: bool = Field(default = False)

    patient:int = Field(...)


class Esthetic(EstheticCreate):
    id: int = Field(...)
    is_done: bool = Field(default = False)
    created_at: datetime = Field(default = datetime.now())
