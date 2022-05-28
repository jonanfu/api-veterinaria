from datetime import datetime

from peewee import *

from app.v1.model.base_model import BaseModel
from app.v1.model.user_model import User
from app.v1.model.type_vaccine_model import TypeVaccine

#tabla vacunas
class Vaccine(BaseModel):
    date = DateTimeField(default = datetime.now)
    lot = CharField()
    apply_vaccine = BooleanField(default = True)
    expiration = DateTimeField()
    price = FloatField()
    weight = FloatField()
    previous_vaccinations = BooleanField(default = False)
    created_at = DateTimeField(default = datetime.now)

    type_vaccine = ForeignKeyField(TypeVaccine, backref = 'vaccine')
