#Python
from datetime import datetime

#Pydantic
from pydantic import BaseModel
from pydantic import Field


class TypeServiceCreate(BaseModel):
    name:str = Field(...)
    description:str


class TypeService(TypeServiceCreate):
    id: int = Field(...)
  