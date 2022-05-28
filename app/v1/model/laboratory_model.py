from peewee import *

from app.v1.model.base_model import BaseModel

#tabla laboratorio
class Laboratory(BaseModel):
    name = CharField()
    description = CharField()
