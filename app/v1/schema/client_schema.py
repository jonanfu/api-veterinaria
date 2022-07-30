#Python
from datetime import datetime

#Pydantic
from pydantic import BaseModel, EmailStr
from pydantic import Field


class ClientCreate(BaseModel):

    full_name:str = Field(
        ...,
    #    max_length = 1,
    #    min_length = 50,
        example = 'first name'
    )
    phone:str = Field(
        ...,
    #    min_length = 8,
    #    max_length = 13,
        example = '0912345678'
    )
    address:str = Field(
        ...,
    #    min_length = 1,
    #    max_length = 150,
        example = 'Calle viva 123'
    )
    identification_card:str = Field(
        ...,
    #    max_length = 6,
    #    min_length = 10,
        example = '0401002003'
    )
    email: EmailStr = Field(
        ...,
        example = 'user@gmail.com'
    )
    city:str = Field(
        ...,
    #    max_length = 5,
    #    min_length = 50,
        example = 'city'
    )


class Client(ClientCreate):
    id: int = Field(...)
