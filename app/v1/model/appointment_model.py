from datetime import datetime

from peewee import *

from app.v1.model.base_model import BaseModel
from app.v1.model.user_model import User
from app.v1.model.type_appointment_model import TypeAppointment
from app.v1.model.patient_model import Patient
from app.v1.model.client_model import Client

#Tabla citas
class Appointment(BaseModel):
    phone = CharField()
    email = CharField()
    date = DateTimeField(default = datetime.now)
    hour = DateTimeField(default = datetime.now)
    reason = CharField()
    internal_notes = CharField()
    activate_reminder = BooleanField(default = False)
    created_at = DateTimeField(default = datetime.now)

    user = ForeignKeyField(User, backref = 'appointment')
    type_appointment = ForeignKeyField(TypeAppointment, backref = 'appointment')
    patient = ForeignKeyField(Patient, backref =  'appointment')
    client = ForeignKeyField(Client, backref = 'appointment')
