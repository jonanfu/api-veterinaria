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
    parameters = Field(...)
    date: Optional[date] = Field(default = datetime.now)

class Hospitalization(HospitalizationCreate):
    id: int = Field(...)
    is_done: bool = Field(default = False)
    created_at: datetime = Field(default = datetime.now())
