from curses.ascii import ETB
from fastapi import HTTPException, status

from app.v1.schema import detail_sale_schema
from app.v1.schema import sale_schema
from app.v1.schema import product_schema
from app.v1.model import detail_sale_model as DetailSaleModel

def create_detail_sale(
    detail_purchase: detail_sale_schema.DetailSaleCreate,
    sale: sale_schema.Sale, 
    product: product_schema.Product):
    pass

def get_detail_sales():
    pass

def get_detail_sale(
    detail_purchase_id: int,
    ):
    pass

def update_detail_sale(
    detail_sale_id: int,
    sale: sale_schema.Sale, 
    product: product_schema.Product,
    ):
    pass

def delete_detail_sale(detail_sale_id: int, purchase: sale_schema.Sale):
    pass
