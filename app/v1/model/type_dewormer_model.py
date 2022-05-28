from datetime import datetime

from peewee import *

from app.v1.model.base_model import BaseModel

#tabla tipo desparacitante
class TypeDewormer(BaseModel):
    name = CharField()
    description = CharField()
