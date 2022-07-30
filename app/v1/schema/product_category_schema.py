#Python

#Pydantic
from pydantic import BaseModel
from pydantic import Field


class ProductCategoryCreate(BaseModel):
    name:str = Field(...)
    photo:str
    description:str


class ProductCategory(ProductCategoryCreate):
    id: int = Field(...)
