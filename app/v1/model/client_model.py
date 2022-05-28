from peewee import *

from app.v1.model.base_model import BaseModel

#tabla cliente
class Client(BaseModel):
    full_name = CharField()
    phone = CharField()
    address = CharField()
    identification_card = CharField(max_length = 10)
    email = CharField()
    city = CharField()
