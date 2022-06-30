from fastapi import HTTPException, status

from app.v1.schema import product_category_schema
from app.v1.model.product_category_model import ProductCategory as ProductCategoryModel

def create_product_category(product_category: product_category_schema.ProductCategoryCreate):
    pass

def get_product_categories():
    pass

def get_product_category(product_category_id: int):
    pass

def update_product_category(product_category_id: int, product_category: product_category_schema.ProductCategoryUpdate):
    pass

def delete_product_category(product_category_id: int):
    pass
