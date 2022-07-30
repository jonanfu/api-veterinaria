#Python
from datetime import datetime

#Pydantic
from pydantic import BaseModel
from pydantic import Field

# modelos para la raza
class BreedCreate(BaseModel):
    name:str = Field(
        ...,
        example = 'nombre de raza'
    )
    description:str
    species:int = Field(...)



class Breed(BreedCreate):
    id: int = Field(...)
   