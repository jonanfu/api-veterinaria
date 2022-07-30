from fastapi import APIRouter, Depends, Body
from fastapi import status
from fastapi import Query
from fastapi import Path

from typing import List, Optional

from app.v1.schema import type_appointment_schema
from app.v1.service import type_appointment_service
from app.v1.utils.db import get_db
from app.v1.schema.user_schema import User
from app.v1.service.auth_service import get_current_user

router = APIRouter(prefix = '/api/v1/type_appointment')


@router.post (
    '/',
    tags = ['type_appointment'],
    status_code = status.HTTP_201_CREATED,
    response_model = type_appointment_schema.TypeAppointment,
    dependencies = [Depends(get_db)]
)
def create_type_appointment (
    type_appointment: type_appointment_schema.TypeAppointmentCreate = Body(...)):
    return type_appointment_service.create_type_appointment(type_appointment)


@router.get (
    '/',
    tags = ['type_appointment'],
    status_code = status.HTTP_200_OK,
    response_model = List[type_appointment_schema.TypeAppointment],
    dependencies = [Depends(get_db)]
)
def get_type_appointment():
    return type_appointment_service.get_type_appointment()


@router.get (
    '/{type_appointment_id}',
    tags = ['type_appointment'],
    status_code = status.HTTP_200_OK,
    response_model = type_appointment_schema.TypeAppointment,
    dependencies = [Depends(get_db)]
)
def get_type_appointment(
    type_appointment_id: int = Path (
        ...,
        gt=0
    )
):
    return type_appointment_service.get_type_appointment(type_appointment_id)


@router.patch (
    '/{type_appointment_id}/update',
    tags = ['type_appointment'],
    status_code = status.HTTP_200_OK,
    response_model = type_appointment_schema.TypeAppointment,
    dependencies=[Depends(get_db)]
)
def type_appointment_update (
    type_appointment_id: int = Path(
        ...,
        gt=0
    ),
    type_appointment: type_appointment_schema.TypeAppointment = Body(...)
):
    return type_appointment_service.update_type_appointment(type_appointment_id,
        name = type_appointment.name,
        description = type_appointment.description
        ) 


@router.delete(
    "/{type_appointment_id}/",
    tags=["type_appointment"],
    status_code=status.HTTP_200_OK,
    dependencies=[Depends(get_db)]
)
def delete_type_appointment(
    type_appointment_id: int = Path(
        ...,
        gt=0
    )
):
    type_appointment_service.delete_type_appointment(type_appointment_id)

    return {
        'msg': 'type_appointment has been deleted sucessfully'
    }
