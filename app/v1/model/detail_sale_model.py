from peewee import *

from app.v1.model.base_model import BaseModel
from app.v1.model.sale_model import Sale
from app.v1.model.product_model import Product

#tabla detalle ventas
class DetailSale(BaseModel):
    amount = IntegerField()
    price = FloatField()
    tax = FloatField()
    subtotal = FloatField()
    discount = FloatField()

    sale = ForeignKeyField(Sale, backref = 'detail_sale')
    product = ForeignKeyField(Product, backref = 'detail_sale')
