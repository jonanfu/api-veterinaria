#Python
from datetime import datetime

#Pydantic
from pydantic import BaseModel
from pydantic import Field


class ConsultationCreate(BaseModel):
    date: Optional[date] = Field(default = datetime.now)
    reason_visit:str = Field(
        ...,
        min_length = 1,
        max_length = 150,
        example = 'Reason visit'
    )
    anommesis:str = Field(
        min_length = 10,
        max_length = 150,
        example = 'Anommesis'
    )
    physical_exam:str = Field(
        ...,
        min_length = 10,
        max_length = 255,
        example = 'Phisical exam'
    )
    diagnosis = Field(
        ...,
        min_length = 10,
        max_length = 255,
        example = 'Examen diagnosis'
    )
    pathology:str = Field(
        ...,
        min_length = 10,
        max_length = 255,
        example = 'pathology'
    )
    treatment:str = Field(
        min_length = 1,
        max_length = 255,
        example = 'Trealment'
    )
    recipe:str = Field(
        min_length = 1,
        max_length = 255,
        example = 'Recipe'
    )
    price:float = Field(...)
    send_whatsapp:bool = Field(default  = False)
    send_email:bool = Field(default = False)
    send_sms:bool = Field(default = False)
    form_payment:str = Field(...)
    is_paid:bool = Field(default = False)

    user:int = Field(...)
    vaccine:int = Field(..)
    dewormer:int = Field(..)
    patient:int = Field(..)


class Consultation(ConsultationCreate):
    id: int = Field(...)
    is_done: bool = Field(default = False)
    created_at: datetime = Field(default = datetime.now())
