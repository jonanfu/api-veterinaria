#Python
from datetime import datetime

#Pydantic
from pydantic import BaseModel, EmailStr
from pydantic import Field


class ProviderCreate(BaseModel):
    name:str = Field(...)
    phone:str = Field(
        ...,
        max_length = 10
    )
    ruc:str = Field(
        min_length = 13
    )
    email:EmailStr
    country:str = Field(...)
    province:str = Field(...)
    city:str = Field(...)
    address:str = Field(...)
    postal_code:str



class Provider(ProviderCreate):
    id: int = Field(...)
    