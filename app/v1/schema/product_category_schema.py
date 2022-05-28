#Python
from datetime import datetime

#Pydantic
from pydantic import BaseModel
from pydantic import Field


class ProductCategoryCreate(BaseModel):
    name:str = Field(...)
    photo:str
    description:str


class ProductCategory(ProductCategoryCreate):
    id: int = Field(...)
    is_done: bool = Field(default = False)
    created_at: datetime = Field(default = datetime.now())
