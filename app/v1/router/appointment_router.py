from fastapi import APIRouter, Depends, Body
from fastapi import status
from fastapi import Query
from fastapi import Path

from typing import List, Optional

from app.v1.schema import appointment_schema
from app.v1.service import appointment_service
from app.v1.utils.db import get_db
from app.v1.schema.user_schema import User
from app.v1.service.auth_service import get_current_user

router = APIRouter(prefix = '/api/v1/appointment')

@router.post (
    '/',
    tags = ['appointment'],
    status_code = status.HTTP_201_CREATED,
    response_model = appointment_schema.Appointment,
    dependencies = [Depends(get_db)]
)
def create_appointment (
    appointment: appointment_schema.AppointmentCreate = Body(...),
    current_user: User = Depends(get_current_user)):
    return appointment_service.create_appointment(appointment, current_user)

    


@router.get (
    '/',
    tags = ['appointment'],
    status_code = status.HTTP_200_OK,
    response_model = List[appointment_schema.Appointment],
    dependencies = [Depends(get_db)]
)
def get_appointments(
    current_user: User = Depends(get_current_user)):
    return appointment_service.get_appointments(current_user)

@router.patch (
    '/{appointment_id}',
    tags = ['appointment'],
    status_code = status.HTTP_200_OK,
    response_model = appointment_schema.Appointment,
    dependencies = [Depends(get_db)]
)
def update_appointment(
    appointment_id: int = Path(
        ...,
        gt = 0
    ),
    appointment: appointment_schema.Appointment = Body(...),
    #current_user: User = Depends(get_current_user)

):
    return appointment_service.update_appointment(appointment_id = appointment_id,
        phone = appointment.phone,
        email = appointment.email,
        date= appointment.date,
        hour = appointment.hour,
        reason = appointment.reason,
        internal_notes = appointment.internal_notes,
        activate_reminder = appointment.activate_reminder,
        #user = current_user,
        type_appointment = appointment.type_appointment,
        patient = appointment.patient,
        client = appointment.client
        )

    

@router.delete(
    '/{appointment_id}',
    tags = ['appointment'],
    status_code = status.HTTP_200_OK,
    dependencies = [Depends(get_db)]
)
def delete_appointment(
    appintment_id: int = Path(
        ...,
        gt = 0
    ),
    current_user: User = Depends(get_current_user)
):
    appointment_service.delete_appointment(appintment_id, current_user)

    return {
        'msg': 'Appointment has been deleted sucessfully'
    }
