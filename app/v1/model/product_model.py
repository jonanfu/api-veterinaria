from peewee import *

from app.v1.model.base_model import BaseModel
from app.v1.model.product_category_model import ProductCategory
from app.v1.model.provider_model import Provider

#tabla productos
class Product(BaseModel):
    name = CharField()
    internal_code = CharField()
    barcode = CharField()
    price = FloatField()
    stock = IntegerField()
    minimun_amount = IntegerField()
    due_date = DateTimeField()
    location = CharField()

    product_category = ForeignKeyField(ProductCategory, backref = 'product')
    provider = ForeignKeyField(Provider, backref = 'product')
