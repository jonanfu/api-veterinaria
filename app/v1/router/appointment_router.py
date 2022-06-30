from fastapi import APIRouter, Depends, Body
from fastapi import status
from fastapi import Query
from fastapi import Path

from typing import List, Optional

from app.v1.schema import appointment_schema
from app.v1.service import appointment_service
from app.v1.utils.db import get_db
from app.v1.schema.user_schema import User
from app.v1.schema.type_appointment_schema import TypeAppointment
from app.v1.schema.patient_schema import Patient
from app.v1.schema.client_shema import Client
from app.v1.service.auth_service import get_current_user

router = APIRouter(prefix = '/api/v1/appointment')

@router.post (
    '/',
    tags = ['appointment'],
    status_code = status.HTTP_201_CREATED,
    response_model = appointment_schema.Appointment,
    dependencies = [Depends(get_db)]
)
def create_appointment ():
    pass


@router.get (
    '/',
    tags = ['appointment'],
    status_code = status.HTTP_200_OK,
    response_model = List[appointment_schema.Appointment],
    dependencies = [Depends(get_db)]
)
def get_appointments():
    pass

@router.patch (
    '/{appointment_id}',
    tags = ['appointment'],
    status_code = status.HTTP_200_OK,
    response_model = appointment_schema.Appointment,
    dependencies = [Depends(get_db)]
)
def update_appointment():
    pass

@router.delete(
    '/{appointment_id}',
    tags = ['appointment'],
    status_code = status.HTTP_200_OK,
    dependencies = [Depends(get_db)]
)
def delete_appointment():
    pass
