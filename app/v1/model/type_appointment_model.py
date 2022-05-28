from datetime import datetime

from peewee import *

from app.v1.model.base_model import BaseModel

#tabla tipo citas
class TypeAppointment(BaseModel):
    name = CharField()
    description = CharField()
