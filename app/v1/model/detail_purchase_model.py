from peewee import *

from app.v1.model.base_model import BaseModel
from app.v1.model.purchase_model import Purchase
from app.v1.model.product_model import Product

#tabla detalle compras
class DetailPurchase(BaseModel):
    amount = IntegerField()
    price = FloatField()
    subtotal = FloatField()
    tax = FloatField()
    profit_percentage = FloatField()

    purchase = ForeignKeyField(Purchase, backref = 'detail_purchase')
    product = ForeignKeyField(Product, backref = 'detail_purchase')
