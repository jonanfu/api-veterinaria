#Python
from datetime import datetime

#Pydantic
from pydantic import BaseModel
from pydantic import Field


class PayDaycareCreate(BaseModel):
    time_eat: Optional[date] = Field(default = None)
    notes:str
    admission_date:bool = Field(default = datetime.now)
    departure_date: Optional[date] = Field(default = None)
    moment_payment:str = Field(...)
    price:float = Field(...)
    form_payment:str = Field(...)
    is_paid:bool = Field(default = False)

    patient:int = Field(...)


class PayDaycare(PayDaycareCreate):
    id: int = Field(...)
    is_done: bool = Field(default = False)
    created_at: datetime = Field(default = datetime.now())
