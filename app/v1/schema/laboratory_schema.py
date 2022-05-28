#Python
from datetime import datetime

#Pydantic
from pydantic import BaseModel
from pydantic import Field


class LaboratoryCreate(BaseModel):
    name:str = Field(...)
    description:str = Field(
        ...,
        max_length = 255
        example = 'description'
    )


class Laboratory(LaboratoryCreate):
    id: int = Field(...)
    is_done: bool = Field(default = False)
    created_at: datetime = Field(default = datetime.now())
