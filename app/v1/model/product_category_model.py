from datetime import datetime

from peewee import *

from app.v1.model.base_model import BaseModel

#tabla producto categoria
class ProductCategory(BaseModel):
    name = CharField()
    photo = CharField()
    description = CharField()
