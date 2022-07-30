#Python
from datetime import datetime

#Pydantic
from pydantic import BaseModel
from pydantic import Field


class SaleCreate(BaseModel):
    total:float = Field(...)

class Sale(SaleCreate):
    id: int = Field(...)
    date: datetime = Field(default = datetime.now())
    status:bool = Field(default = True)
