from fastapi import APIRouter, Depends, Body
from fastapi import status
from fastapi import Query
from fastapi import Path

from typing import List, Optional

from app.v1.schema import clinic_schema
from app.v1.service import clinic_service
from app.v1.utils import get_db
from app.v1.schema.user_schema import User
from app.v1.service.auth_service import get_current_user

router = APIRouter(prefix = '/api/v1/clinic')


@router.post (
    '/',
    tags = ['clinic'],
    status_code = status.HTTP_201_CREATED,
    response_model = clinic_schema.Clinic,
    dependencies = [Depends(get_db)]
)
def create_clinic (
    todo: clinic_schema.ClinicCreate = Body(...),
    current_user: User = Depends(get_current_user)):
    return clinic_service.create_clinic(clinic, current_user)


@router.get (
    '/',
    tags = ['clinic'],
    status_code = status.HTTP_200_OK,
    response_model = List[clinic_schema.Clinic],
    dependencies = [Depends(get_db)]
)
def get_clinic(
    is_done: Optional[bool] = Query(None),
    current_user: User = Depends(get_current_user)
):
    return clinic_service.get_clinics(current_user, is_done)


@router.get (
    '/{clinic_id}',
    tags = ['clinic'],
    status_code = status.HTTP_200_OK,
    response_model = clinic_schema.Clinic,
    dependencies = [Depends(get_db)]
)
def get_clinic(
    task_id: int = Path (
        ...,
        gt=0
    ),
    current_user: User = Depends(get_current_user)
):
    return clinic_service.get_task(clinic_id, current_user)


@router.patch (
    '/{task_id}/update',
    tags = ['clinic'],
    status_code = status.HTTP_200_OK,
    response_model = clinic_schema.Clinic,
    dependencies=[Depends(get_db)]
)
def clinic_update (
    task_id: int = Path(
        ...,
        gt=0
    ),
    current_user: User = Depends(get_current_user)
):
    return clinic_service.update_status_task(clinic_id, current_user)


@router.delete(
    "/{clinic_id}/",
    tags=["clinic"],
    status_code=status.HTTP_200_OK,
    dependencies=[Depends(get_db)]
)
def delete_clinic(
    task_id: int = Path(
        ...,
        gt=0
    ),
    current_user: User = Depends(get_current_user)
):
    clinic_service.delete_clinic(clinic_id, current_user)

    return {
        'msg': 'clinic has been deleted sucessfully'
    }
