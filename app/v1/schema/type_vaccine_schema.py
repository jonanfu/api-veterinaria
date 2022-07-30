#Python
from datetime import datetime

#Pydantic
from pydantic import BaseModel
from pydantic import Field


class TypeVaccineCreate(BaseModel):
    name: str = Field()
    description:str



class TypeVaccine(TypeVaccineCreate):
    id: int = Field(...)

