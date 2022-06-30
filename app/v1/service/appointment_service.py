from fastapi import HTTPException, status

from app.v1.schema import appointment_schema
from app.v1.schema import user_schema
from app.v1.model.appointment_model import Appointment as AppointmentModel 

def create_appointment(appointment: appointment_schema.AppointmentCreate, user: user_schema.User):
    db_appointment = AppointmentModel(
        title = appointment.title,
        user_id = user.id
    )

    db_appointment.save()

    return appointment_schema.Appointment(
        id = db_appointment.id,
        title = db_appointment.title,
        is_done = db_appointment.is_done,
        created_at = db_appointment.created_at
    )
def get_appointments(user: user_schema.User, is_done: bool = None):
    if(is_done is None):
        appointments_by_user = AppointmentModel.filter(AppointmentModel.user_id == user.id).order_by(AppointmentModel.created_at.desc())
    else:
        appointments_by_user = AppointmentModel.filter((AppointmentModel.user_id == user.id) & (AppointmentModel.is_done == is_done )).order_by(AppointmentModel.created_at.desc())

    list_appointments = []
    for appointment in appointments_by_user:
        list_appointments.append(
            appointment_schema.Appointment(
                id = appointment.id,
                title = appointment.title,
                is_done = appointment.is_done,
                created_at = appointment.created_at
            )
        )

    return list_appointments

def update_appointment(appointment_id: int, appointment: appointment_schema.AppointmentUpdate, user: user_schema.User):
    pass

def delete_appointment(appointment_id: int, user: user_schema.User):
    pass

