#Python
from datetime import datetime

#Pydantic
from pydantic import BaseModel
from pydantic import Field


class DetailPurchaseCreate(BaseModel):
    amount:int = Field(...)
    price:float = Field(...)
    subtotal:float = Field(...)
    tax:float = Field(...)
    profit_percentage:float = Field(...)
    
    purchase:int = Field(...)
    product:int = Field(...)

class DetailPurchase(DetailPurchaseCreate):
    id: int = Field(...)