#Python
from datetime import datetime

#Pydantic
from pydantic import BaseModel
from pydantic import Field


class SpeciesCreate(BaseModel):
    name:str = Field(...)
    description:str

class Species(SpeciesCreate):
    id: int = Field(...)
    created_at: datetime = Field(default = datetime.now())
