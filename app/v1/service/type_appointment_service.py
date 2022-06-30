from fastapi import HTTPException, status

from app.v1.schema import type_appointment_schema
from app.v1.model.type_appointment_model import TypeAppointment as TypeAppointmentModel

def create_type_appointment(type_appointment: type_appointment_schema.TypeAppointmentCreate):
    pass

def get_type_appointments():
    pass

def get_type_appointment(type_appointment_id: int):
    pass

def update_type_appointment(type_appointment_id: int, type_appointment: type_appointment_schema.TypeAppointmentUpdate):
    pass

def delete_type_appointment(type_appointment_id: int):
    pass
