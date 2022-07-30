#Python
from datetime import datetime

#Pydantic
from pydantic import BaseModel
from pydantic import Field


class ClinicCreate(BaseModel):

    name:str = Field(
        ...,
        max_length = 10,
        min_length = 150,
        example = 'name'
    )
    addres:str = Field(
        ...,
        min_length = 10,
        max_length = 150,
        example = 'addres'
    )
    city:str = Field(
        ...,
        min_length = 1,
        max_length = 50,
        example = 'city'
    )
    phone:str = Field(
        ...,
        min_length = 8,
        max_length = 13,
        example = '0912345678'
    )
    ruc:str = Field(
        ...,
        min_length = 13,
        max_length = 13,
        example = '1002003001100'
    )
    user:int = Field(...)

class Clinic(ClinicCreate):
    id: int = Field(...)
    created: datetime = Field(default = datetime.now())
