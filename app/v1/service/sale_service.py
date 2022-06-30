from fastapi import HTTPException, status

from app.v1.schema import sale_schema
from app.v1.model.sale_model import Sale as SaleModel

def create_sale(sale: sale_schema.SaleCreate):
    pass

def get_sales():
    pass

def get_sale(sale_id: int):
    pass

def update_sale(sale_id: int, sale: sale_schema.SaleUpdate):
    pass

def delete_sale(sale_id: int):
    pass

