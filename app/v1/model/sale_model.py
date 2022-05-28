from datetime import datetime

from peewee import *

from app.v1.model.base_model import BaseModel

#tabla ventas
class Sale(BaseModel):
    date = DateTimeField(default = datetime.now)
    total = FloatField()
    status = BooleanField(default = True)
