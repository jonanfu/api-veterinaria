from datetime import datetime

from peewee import *

from app.v1.model.base_model import BaseModel
from app.v1.model.user_model import User
from app.v1.model.vaccine_model import Vaccine
from app.v1.model.dewormer_model import Dewormer
from app.v1.model.patient_model import Patient

#tabla consultas
class Consultation(BaseModel):
    date = DateTimeField(default = datetime.now)
    reason_visit = CharField()
    anommesis = CharField()
    physical_exam = CharField()
    diagnosis = CharField()
    pathology = CharField()
    treatment = CharField()
    recipe = CharField()
    price = FloatField()
    send_whatsapp = BooleanField(default  = False)
    send_email = BooleanField(default = False)
    send_sms = BooleanField(default = False)
    form_payment = CharField()
    is_paid = BooleanField(default = False)
    created_at = DateTimeField(default = datetime.now)

    user = ForeignKeyField(User, backref = 'consultations')
    vaccine = ForeignKeyField(Vaccine, backref = 'consultations')
    dewormer = ForeignKeyField(Dewormer, backref = 'consultations')
    patient = ForeignKeyField(Patient, backref = 'consultations')
