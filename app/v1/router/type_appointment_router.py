from fastapi import APIRouter, Depends, Body
from fastapi import status
from fastapi import Query
from fastapi import Path

from typing import List, Optional

from app.v1.schema import type_appointment_schema
from app.v1.service import type_appointment_service
from app.v1.utils import get_db
from app.v1.schema.user_schema import User
from app.v1.service.auth_service import get_current_user

router = APIRouter(prefix = '/api/v1/type_appointment')


@router.post (
    '/',
    tags = ['type_appointment'],
    status_code = status.HTTP_201_CREATED,
    response_model = type_appointment_schema.Clinic,
    dependencies = [Depends(get_db)]
)
def create_type_appointment (
    todo: type_appointment_schema.ClinicCreate = Body(...),
    current_user: User = Depends(get_current_user)):
    return type_appointment_service.create_type_appointment(type_appointment, current_user)


@router.get (
    '/',
    tags = ['type_appointment'],
    status_code = status.HTTP_200_OK,
    response_model = List[type_appointment_schema.Clinic],
    dependencies = [Depends(get_db)]
)
def get_type_appointment(
    is_done: Optional[bool] = Query(None),
    current_user: User = Depends(get_current_user)
):
    return type_appointment_service.get_type_appointments(current_user, is_done)


@router.get (
    '/{type_appointment_id}',
    tags = ['type_appointment'],
    status_code = status.HTTP_200_OK,
    response_model = type_appointment_schema.Clinic,
    dependencies = [Depends(get_db)]
)
def get_type_appointment(
    task_id: int = Path (
        ...,
        gt=0
    ),
    current_user: User = Depends(get_current_user)
):
    return type_appointment_service.get_type_appointment(type_appointment_id, current_user)


@router.patch (
    '/{task_id}/update',
    tags = ['type_appointment'],
    status_code = status.HTTP_200_OK,
    response_model = type_appointment_schema.Clinic,
    dependencies=[Depends(get_db)]
)
def type_appointment_update (
    task_id: int = Path(
        ...,
        gt=0
    ),
    current_user: User = Depends(get_current_user)
):
    return type_appointment_service.update_status_task(type_appointment_id, current_user)


@router.delete(
    "/{type_appointment_id}/",
    tags=["type_appointment"],
    status_code=status.HTTP_200_OK,
    dependencies=[Depends(get_db)]
)
def delete_type_appointment(
    task_id: int = Path(
        ...,
        gt=0
    ),
    current_user: User = Depends(get_current_user)
):
    type_appointment_service.delete_type_appointment(type_appointment_id, current_user)

    return {
        'msg': 'type_appointment has been deleted sucessfully'
    }
