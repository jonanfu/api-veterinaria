#Python

#Pydantic
from pydantic import BaseModel
from pydantic import Field


class LaboratoryCreate(BaseModel):
    name:str = Field(...)
    description:str = Field(
        ...,
        max_length = 255,
        example = 'description'
    )


class Laboratory(LaboratoryCreate):
    id: int = Field(...)