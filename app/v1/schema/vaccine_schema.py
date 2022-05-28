#Python
from datetime import datetime

#Pydantic
from pydantic import BaseModel
from pydantic import Field


class VaccineCreate(BaseModel):
    date: Optional[date] = Field(default = datetime.now)
    lot:str = Field(...)
    apply_vaccine:bool = Field(default = True)
    expiration: Optional[date] = Field(default = None)
    price:float = Field(...)
    weight:float = Field(...)
    previous_vaccinations:bool = Field(default = False)

    type_vaccine:int = Field(...)


class Vaccine(VaccineCreate):
    id: int = Field(...)
    created_at: datetime = Field(default = datetime.now())
