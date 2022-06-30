from fastapi import HTTPException, status

from app.v1.schema import purchase_schema
from app.v1.model.purchase_model import Purchase as PurchaseModel

def create_purchase(purchase: purchase_schema.PurchaseCreate):
    pass

def get_purchases():
    pass

def get_purchase(purchase_id: int):
    pass

def update_purchase(purchase_id: int, purchase: purchase_schema.PurchaseUpdate):
    pass

def delete_purchase(purchase_id: int):
    pass
