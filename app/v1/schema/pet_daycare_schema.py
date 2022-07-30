#Python
from datetime import datetime

#Pydantic
from pydantic import BaseModel
from pydantic import Field


class PetDaycareCreate(BaseModel):
    time_eat: datetime = Field(...)
    notes:str
    departure_date:datetime
    moment_payment:str = Field(...)
    price:float = Field(...)
    form_payment:str = Field(...)
    is_paid:bool = Field(default = False)

    patient:int = Field(...)


class PetDaycare(PetDaycareCreate):
    id: int = Field(...)
    admission_date: datetime = Field(default = datetime.now())
