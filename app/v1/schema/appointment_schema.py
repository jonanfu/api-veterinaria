#Python
from datetime import datetime
from datetime import date
from typing import Optional, List

#Pydantic
from pydantic import BaseModel, EmailStr
from pydantic import Field


class AppointmentCreate(BaseModel):
    phone: str = Field(
        ...,
        min_length = 1,
        max_length = 10
    )
    email: EmailStr
    date: Optional[date] = Field(default=None)
    hour: Optional[date] = Field(default=None)
    reason:str
    initer_notes:str
    activate_reminder: Optional[date] = Field(default=None)
    user:int = Field(...)
    type_appointment:int = Field(...)
    patient:int = Field(...)
    client:int = Field(...)



class Appointment(AppointmentCreate):
    id: int = Field(...)
    created_at: datetime = Field(default = datetime.now())
