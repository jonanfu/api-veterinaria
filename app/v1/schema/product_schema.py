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
    due_date: Optional[date] = Field(default = None)
    location:str

    product_category:int = Field(...)



class Product(ProductCreate):
    id: int = Field(...)
    is_done: bool = Field(default = False)
    created_at: datetime = Field(default = datetime.now())
