from datetime import datetime

from peewee import *

from app.v1.model.base_model import BaseModel
from app.v1.model.patient_model import Patient

#tabla estetica
class Esthetic(BaseModel):
    date = DateTimeField(default = datetime.now)
    hour = DateTimeField()
    activate_notification = BooleanField()
    price = FloatField()
    form_payment = CharField()
    is_paid = BooleanField()

    patient = ForeignKeyField(Patient, backref = 'esthetic')
