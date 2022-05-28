#Python
from datetime import datetime

#Pydantic
from pydantic import BaseModel
from pydantic import Field


class ClientCreate(BaseModel):

    full_name:str = Field(
        ...,
        max_length = 1,
        min_length = 50
        example = 'firt_name'
    )
    phone:int = Field(
        ...,
        min_length = 8
        max_length = 13
        example = '0912345678'
    )
    address:str = Field(
        ...,
        min_length = 10,
        max_length = 150,
        example = 'Calle viva 123'
    )
    identification_card:str = Field(
        ...,
        min_length = 6,
        max_length = 10,
        example = '0401002003001'
    )
    email: EmailStr
    city:str = Field(
        ...,
        min_length = 5,
        max_length = 50
        example = 'city'
    )

    title: str = Field(
        ...,
        min_length = 1,
        max_length = 60,
        example = 'My first task'
    )


class Client(ClientCreate):
    id: int = Field(...)
    is_done: bool = Field(default = False)
    created_at: datetime = Field(default = datetime.now())
