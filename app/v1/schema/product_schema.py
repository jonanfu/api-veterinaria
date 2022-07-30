#Python
from datetime import datetime

#Pydantic
from pydantic import BaseModel
from pydantic import Field


class ProductCreate(BaseModel):
    name:str = Field(...)
    internal_code:str
    barcode:str = Field(...)
    price:float = Field(...)
    stock:int = Field(...)
    minimun_amount:int = Field(...)
    due_date: datetime = Field(...)
    location:str

    product_category:int = Field(...)
    provider:int = Field(...)


class Product(ProductCreate):
    id: int = Field(...)
   