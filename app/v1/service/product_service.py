from fastapi import HTTPException, status

from app.v1.schema import product_schema
from app.v1.schema import product_category_schema
from app.v1.schema import provider_schema
from app.v1.model import product_model as ProductModel

def create_product(
    product: product_schema.ProductCreate, 
    product_category: product_category_schema.ProductCategory,
    provider: provider_schema.Provider
    ):
    pass

def get_products():
    pass

def get_product(product_id: int):
    pass

def update_product(product_id: int, product: product_schema.ProductUpdate):
    pass

def delete_product(product_id: int):
    pass
