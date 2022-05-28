from datetime import datetime

from peewee import *

from app.v1.model.base_model import BaseModel

#tabla compras
class Purchase(BaseModel):
    date = DateTimeField(default = datetime.now)
    total = FloatField()
    status = BooleanField(default = True)
    image = CharField()
