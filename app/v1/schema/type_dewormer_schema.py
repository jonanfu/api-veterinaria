#Python
from datetime import datetime

#Pydantic
from pydantic import BaseModel
from pydantic import Field


class TypeDewormerCreate(BaseModel):
    name:str = Field(...)
    description:str

class TypeDewormer(TypeDewormerCreate):
    id: int = Field(...)
  