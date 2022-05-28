from datetime import datetime

from peewee import *

from app.v1.model.base_model import BaseModel

#tabla especies
class Species(BaseModel):
    name = CharField()
    description = CharField()
