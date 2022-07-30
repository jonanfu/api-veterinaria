#Python
from datetime import datetime

#Pydantic
from pydantic import BaseModel
from pydantic import Field


class VaccineCreate(BaseModel):
    date: datetime = Field(...)
    lot:str = Field(...)
    apply_vaccine:bool = Field(default = True)
    expiration: datetime = Field(...)
    price:float = Field(...)
    weight:float = Field(...)
    previous_vaccinations:bool = Field(default = False)

    type_vaccine:int = Field(...)


class Vaccine(VaccineCreate):
    id: int = Field(...)
    created_at: datetime = Field(default = datetime.now())
