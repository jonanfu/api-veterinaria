from datetime import datetime

from peewee import *

from app.v1.model.base_model import BaseModel
from app.v1.model.patient_model import Patient

#tabla hospitalizationes
class Hospitalization(BaseModel):
    diagnosis = CharField()
    aspect = CharField()
    weight = FloatField()
    feeding = CharField()
    observation = CharField()
    other_indications = CharField()
    parameters = CharField()
    date = DateTimeField(default = datetime.now)

    patient = ForeignKeyField(Patient, backref = 'hospitalization')
