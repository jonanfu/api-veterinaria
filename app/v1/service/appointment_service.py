from http import client
from turtle import title
from fastapi import HTTPException, status

from app.v1.schema import appointment_schema, type_vaccine_schema
from app.v1.schema import user_schema
from app.v1.model.appointment_model import Appointment as AppointmentModel 

def create_appointment(appointment: appointment_schema.AppointmentCreate, user: user_schema.User):
    db_appointment = AppointmentModel(
        phone = appointment.phone,
        email = appointment.email,
        date = appointment.date,
        hour = appointment.hour,
        reason = appointment.reason,
        internal_notes = appointment.internal_notes,
        activate_reminder = appointment.activate_reminder,
        create_at = appointment.create_at,

        user = user.id,
        type_appointment = appointment.type_appointment,
        patient = appointment.patient,
        client = appointment.client
    )

    db_appointment.save()

    return appointment_schema.Appointment(
        id = db_appointment.id,
        phone = db_appointment.phone,
        email = db_appointment.email,
        date = db_appointment.date,
        hour = db_appointment.hour,
        reason = appointment.reason,
        internal_notes = appointment.internal_notes,
        activate_reminder = appointment.activate_reminder,
        created_at = db_appointment.created_at,

        user = db_appointment.user,
        type_appointment = appointment.type_appointment,
        patient = db_appointment.patient,
        client = db_appointment.client
    )


def get_appointments(user: user_schema.User):
   
    appointments_by_user = AppointmentModel.filter(AppointmentModel.user_id == user.id).order_by(AppointmentModel.created_at.desc())

    list_appointments = []
    for appointment in appointments_by_user:
        list_appointments.append(
            appointment_schema.Appointment(
                id = appointment.id,
                phone = appointment.phone,
                email = appointment.email,
                date = appointment.date,
                hour = appointment.hour,
                reason = appointment.reason,
                internal_notes = appointment.internal_notes,
                activate_reminder = appointment.activate_reminder,
                created_at = appointment.created_at,

                user = appointment.user,
                type_appointment = appointment.type_appointment,
                patient = appointment.patient,
                client = appointment.client
            )
        )

    return list_appointments

def get_appointment(appointment_id: int, user: user_schema.User):
    appointment = AppointmentModel.filter((AppointmentModel.id == appointment_id) & (AppointmentModel == user.id)).first()

    if not appointment:
        raise HTTPException (
            status_code = status.HTTP_404_NOT_FOUND,
            detail = 'Appointment not found'
        )

    return appointment_schema.Appointment(
        id = appointment.id,
        phone = appointment.phone,
        email = appointment.email,
        date = appointment.date,
        hour = appointment.hour,
        reason = appointment.reason,
        internal_notes = appointment.internal_notes,
        activate_reminder = appointment.activate_reminder,
        create_at = appointment.crete_at,

        user = appointment.user,
        type_appointment = appointment.type_appointment,
        patient = appointment.patient,
        client = appointment.client
    )
def update_appointment(appointment_id: int,
    phone: str = None,
    email: str = None,
    date: str = None,
    hour: str = None,
    reason: str = None,
    internal_notes: str = None,
    activate_reminder: bool = None,
    user: user_schema.User = None,
    type_appointment: int = None,
    patient: int = None, 
    client: int = None
    ):
    
    appointment = AppointmentModel.filter((AppointmentModel.id == appointment_id) & AppointmentModel == user.id)
    
    if not appointment:
        raise HTTPException(
            status_code = status.HTTP_404_NOT_FOUND,
            detail = 'Appointment not found'
        )
    
    appointment.phone = phone or appointment.phone
    appointment.email = email or appointment.email
    appointment.date = date or appointment.date
    appointment.hour = hour or appointment.hour
    appointment.reason = reason or appointment.reason
    appointment.internal_notes = internal_notes or appointment.internal_notes
    appointment.activate_reminder = activate_reminder or appointment.activate_reminder
    
    appointment.type_appointment = type_appointment or appointment.type_appointment
    appointment.patient = patient or appointment.patient
    appointment.client = client or appointment.client

    return appointment_schema.Appointment (
        id = appointment.id,
        phone = appointment.phone,
        email = appointment.email,
        date = appointment.date,
        hour = appointment.hour,
        reason = appointment.reason,
        internal_notes = appointment.internal_notes,
        activate_reminder = appointment.activate_reminder,
        created_at = appointment.created_at,

        user = appointment.user,
        type_appointment = appointment.type_appointment,
        patient = appointment.patient,
        client = appointment.client
        
    )


def delete_appointment(appointment_id: int, user: user_schema.User):
    appointment = AppointmentModel.filter((AppointmentModel.id == appointment_id) & (AppointmentModel == user.id)).first()

    if not appointment:
        raise HTTPException (
            status_code = status.HTTP_404_NOT_FOUND,
            detail = 'Appointment not found'
        )

    appointment.delete_instance()


