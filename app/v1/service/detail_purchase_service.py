from fastapi import HTTPException, status

from app.v1.schema import detail_purchase_schema
from app.v1.schema import purchase_schema
from app.v1.schema import product_schema
from app.v1.model import detail_purchase_model as DetailPurchaseModel

def create_detail_purchase(
    detail_purchase: detail_purchase_schema.DetailPurchaseCreate,
    purchase: purchase_schema.Purchase, 
    product: product_schema.Product):
    pass

def get_detail_purchases():
    pass

def get_detail_purchase(
    detail_purchase_id: int,
    ):
    pass

def update_detail_purchase(
    detail_purchase_id: int,
    purchase: purchase_schema.Purchase, 
    product: product_schema.Product,
    ):
    pass

def delete_detail_purchase(detail_purchase_id: int, purchase: purchase_schema.Purchase):
    pass

