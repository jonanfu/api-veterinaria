#Python
from datetime import datetime

#Pydantic
from pydantic import BaseModel
from pydantic import Field


class PurchaseCreate(BaseModel):
    total:float = Field(...)
    image:str



class Purchase(PurchaseCreate):
    id: int = Field(...)
    date: datetime = Field(default = datetime.now())
    status:bool = Field(default = True)
