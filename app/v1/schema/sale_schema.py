#Python
from datetime import datetime

#Pydantic
from pydantic import BaseModel
from pydantic import Field


class SaleCreate(BaseModel):

    date: Optional[date] = Field(default = datetime.now)
    total:float = Field(...)

class Sale(SaleCreate):
    id: int = Field(...)
    status:bool = Field(default = True)
    created_at: datetime = Field(default = datetime.now())
