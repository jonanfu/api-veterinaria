from datetime import datetime

from peewee import *

from app.v1.model.base_model import BaseModel
from app.v1.model.type_dewormer_model import TypeDewormer

#tabla desparasitante
class Dewormer(BaseModel):
    date = DateTimeField(default = datetime.now)
    apply_deworner = BooleanField(default = False)
    lot = CharField()
    expiration = DateTimeField()
    price = FloatField()
    weight = FloatField()

    type_dewormer = ForeignKeyField(TypeDewormer, backref = 'dewormer')
