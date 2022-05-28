#Python
from datetime import datetime

#Pydantic
from pydantic import BaseModel
from pydantic import Field


class PurchaseCreate(BaseModel):
    date: Optional[date] = Field(default = datetime.now)
    total:float = Field(...)
    status:bool = Field(default = True)
    image:str



class Purchase(PurchaseCreate):
    id: int = Field(...)
    created_at: datetime = Field(default = datetime.now())
