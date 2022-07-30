#Python
from datetime import datetime

#Pydantic
from pydantic import BaseModel
from pydantic import Field


class TypeAppointmentCreate(BaseModel):
    name:str = Field(...)
    description:str


class TypeAppointment(TypeAppointmentCreate):
    id: int = Field(...)
    