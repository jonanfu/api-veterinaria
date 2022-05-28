from peewee import *

from app.v1.model.base_model import BaseModel

#tabla proveedores
class Provider(BaseModel):
    name = CharField()
    phone = CharField(max_length = 10)
    ruc = CharField(max_length = 13)
    email = CharField()
    country = CharField()
    province = CharField()
    city = CharField()
    address = CharField()
    postal_code = CharField()
    is_actived = BooleanField(default = True)
