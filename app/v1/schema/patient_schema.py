#Python
from datetime import datetime

#Pydantic
from pydantic import BaseModel
from pydantic import Field


class PatientCreate(BaseModel):
    name = Field(
        ...,
        min_length = 1
        max_length = 50,
        example = 'name'
    )
    birthday: Optional[date]  = Field(default = datetime.now)
    years:int = Field(...)
    months:int = Field(...)
    gender = Field(...)
    fur = Field(...)
    food_consumer = Field(...)
    is_heat:bool = Field(default = False)
    is_pedigree:bool = Field(default = False)
    is_reproductive:bool = Field(default = False)
    is_castrated:bool = Field(default = False)
    pathologies = Field(...)
    photo = Field(...)
    chip:str
    aggressive:float = Field(...)
    is_dead:bool = Field(default = False)


class Patient(PatientCreate):
    id: int = Field(...)
    is_done: bool = Field(default = False)
    created_at: datetime = Field(default = datetime.now())
