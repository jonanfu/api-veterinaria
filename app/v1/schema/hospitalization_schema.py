#Python
from datetime import datetime

#Pydantic
from pydantic import BaseModel
from pydantic import Field


class HospitalizationCreate(BaseModel):
    diagnosis:str = Field(
        ...,
        min_length = 1,
        max_length = 255,
        example = 'diagnosis'
    )
    aspect:str = Field(
        ...,
        min_length = 1,
        max_length = 255,
        example = 'aspect'
    )
    weight:float = Field(...)
    feeding:str = Field(...)
    observation:str = Field(...)
    other_indications:str = Field(...)
    parameters:str = Field(...)

class Hospitalization(HospitalizationCreate):
    id: int = Field(...)
    date: datetime = Field(default = datetime.now())
