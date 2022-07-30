from fastapi import HTTPException, status

from app.v1.schema import type_appointment_schema
from app.v1.model.type_appointment_model import TypeAppointment as TypeAppointmentModel

def create_type_appointment(type_appointment: type_appointment_schema.TypeAppointmentCreate):
    db_type_appointment = TypeAppointmentModel(
        name = type_appointment.name,
        description = type_appointment.description
    )

    db_type_appointment.save()

    return type_appointment_schema.TypeAppointment(
        id = db_type_appointment.id,
        name = db_type_appointment.name,
        description = db_type_appointment.description
    )

def get_type_appointments():
    type_appointments = TypeAppointmentModel.select().order_by(TypeAppointmentModel.id.desc())

    list_type_appointments = []
    for type_appointment in type_appointments:
        list_type_appointments.append (
            type_appointment_schema.TypeAppointment(
                id = type_appointment.id,
                name = type_appointment.name,
                description = type_appointment.desciption
            )
        )
    return list_type_appointments

def get_type_appointment_by_id(type_appointment_id: int):
    type_appointment = TypeAppointmentModel.filter(TypeAppointmentModel.id == type_appointment_id).first()

    if not type_appointment:
        raise HTTPException (
            status_code = status.HTTP_404_NOT_FOUND,
            detail = "Type appointment not found"
        )

    return type_appointment_schema.TypeAppointment(
        id = type_appointment.id,
        name = type_appointment.name,
        description = type_appointment.description
    )

def update_type_appointment(type_appointment_id: int, 
    name: str = None,
    description: str = None    
    ):

    type_appointment = TypeAppointmentModel.filter(TypeAppointmentModel.id == type_appointment_id).first()

    if not type_appointment:
        raise HTTPException(
            status_code = status.HTTP_404_NOT_FOUND,
            detail = 'Type appointment not found'
        )
    
    type_appointment.name = name or type_appointment.name
    type_appointment.description = description or type_appointment.description

    type_appointment.save()
    return type_appointment_schema.TypeAppointment(
        id = type_appointment.id,
        name = type_appointment.name,
        description = type_appointment.description

    )
def delete_type_appointment(type_appointment_id: int):
    type_appointment = TypeAppointmentModel.filter(TypeAppointmentModel.id == type_appointment_id).first()

    if not type_appointment:
        raise HTTPException(
            status_code = status.HTTP_404_NOT_FOUND,
            detail = 'Type appointment not found'
        )

    type_appointment.delete_instance()
