from datetime import datetime

from peewee import *

from app.v1.model.base_model import BaseModel
from app.v1.model.user_model import User

#tabla clinica
class Clinic(BaseModel):
    name = CharField()
    addres = CharField()
    city = CharField()
    phone = CharField(max_length = 10)
    ruc = CharField(max_length = 13)
    user = ForeignKeyField(User, backref="clinic")
    created = DateTimeField(default = datetime.now)
