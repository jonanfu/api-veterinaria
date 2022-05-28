#Python
from datetime import datetime

#Pydantic
from pydantic import BaseModel
from pydantic import Field


class TypeVaccineCreate(BaseModel):
    name = CharField()
    description:str



class TypeVaccine(TypeVaccineCreate):
    id: int = Field(...)
    created_at: datetime = Field(default = datetime.now())
