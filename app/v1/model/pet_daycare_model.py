from datetime import datetime

from peewee import *

from app.v1.model.base_model import BaseModel
from app.v1.model.patient_model import Patient

#tabla guarderia
class PetDaycare(BaseModel):
    time_eat = DateTimeField()
    notes = CharField()
    admission_date = DateTimeField(default = datetime.now)
    departure_date = DateTimeField()
    moment_payment = CharField()
    price = FloatField()
    form_payment = CharField()
    is_paid = BooleanField(default = False)

    patient = ForeignKeyField(Patient, backref = 'pet_daycare')
