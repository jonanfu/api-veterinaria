#Python
from datetime import datetime

#Pydantic
from pydantic import BaseModel
from pydantic import Field


class DetailSaleCreate(BaseModel):

    amount = Field(
        ...,
        min_length = 1
    )
    price = Field(...)
    tax = Field(...)
    subtotal = Field(...)
    discount = Field(...)

    sale = Field(...)
    product = Field(...)


class DetailSale(DetailSaleCreate):
    id: int = Field(...)
    is_done: bool = Field(default = False)
    created_at: datetime = Field(default = datetime.now())
