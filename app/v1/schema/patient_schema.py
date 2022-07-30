#Python
from datetime import datetime
from http import client

#Pydantic
from pydantic import BaseModel
from pydantic import Field


class PatientCreate(BaseModel):
    name:str = Field(
        ...,
        min_length = 5,
        max_length = 50,
        example = 'name'
    )
    birthday: datetime  = Field(...)
    years:int = Field(...)
    months:int = Field(...)
    gender:str = Field(...)
    fur:str = Field(...)
    food_consumer:str = Field(...)
    is_heat:bool = Field(default = False)
    is_pedigree:bool = Field(default = False)
    is_reproductive:bool = Field(default = False)
    is_castrated:bool = Field(default = False)
    pathologies:str = Field(...)
    photo:str = Field(...)
    chip:str = Field(...)
    aggressive:float = Field(...)
    specie:int = Field(...)
    breed:int = Field(...)
    client:int = Field(...)


class Patient(PatientCreate):
    id: int = Field(...)
    is_dead: bool = Field(default = False)