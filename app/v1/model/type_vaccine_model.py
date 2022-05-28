from datetime import datetime

from peewee import *

from app.v1.model.base_model import BaseModel

#tabla tipo vacunas
class TypeVaccine(BaseModel):
    name = CharField()
    description = CharField()
