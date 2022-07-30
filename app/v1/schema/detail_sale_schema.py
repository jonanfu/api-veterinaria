#Python
from datetime import datetime

#Pydantic
from pydantic import BaseModel
from pydantic import Field


class DetailSaleCreate(BaseModel):

    amount:int = Field(...)
    price:float = Field(...)
    tax:float = Field(...)
    subtotal:float = Field(...)
    discount:float = Field(...)

    sale:int = Field(...)
    product:int = Field(...)


class DetailSale(DetailSaleCreate):
    id: int = Field(...)
   