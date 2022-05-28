#Python
from datetime import datetime

#Pydantic
from pydantic import BaseModel
from pydantic import Field


class DewormerCreate(BaseModel):
    date: Optional[date] = Field(default = datetime.now)
    apply_deworner:bool = Field(default = False)
    lot:str = Field(
        ...,
        min_length = 1,
        max_length = 255,
        example = 'Dewormer'
    )
    expiration: Optional[date] = Field(default = None)
    price:float = Field(...)
    weight:float = Field(...)
    type_dewormer:int = Field(...)


class Dewormer(DewormerCreate):
    id: int = Field(...)
    is_done: bool = Field(default = False)
    created_at: datetime = Field(default = datetime.now())
