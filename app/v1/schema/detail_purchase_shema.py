#Python
from datetime import datetime

#Pydantic
from pydantic import BaseModel
from pydantic import Field


class DetailPurchaseCreate(BaseModel):

    amount:int = Field(
        ...,
        min_length = 1
    )
    price:float = Field(...)
    subtotal:float = Field(...)
    tax:float = Field(...)
    profit_percentage:float = Field(...)
    #
    purchase:int = Field(...)
    product = Field(...)



class DetailPurchase(DetailPurchaseCreate):
    id: int = Field(...)
    is_done: bool = Field(default = False)
    created_at: datetime = Field(default = datetime.now())
