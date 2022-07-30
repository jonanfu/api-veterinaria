#Python
from datetime import datetime

#Pydantic
from pydantic import BaseModel
from pydantic import Field


class DewormerCreate(BaseModel):
    date: datetime = Field(...)
    apply_deworner:bool = Field(default = False)
    lot:str = Field(
        ...,
        min_length = 1,
        max_length = 255,
        example = 'Dewormer'
    )
    expiration: datetime = Field()
    price:float = Field(...)
    weight:float = Field(...)
    type_dewormer:int = Field(...)


class Dewormer(DewormerCreate):
    id: int = Field(...)
    