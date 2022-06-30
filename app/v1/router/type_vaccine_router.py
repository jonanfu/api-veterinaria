from fastapi import APIRouter, Depends, Body
from fastapi import status
from fastapi import Query
from fastapi import Path

from typing import List, Optional

from app.v1.schema import type_vaccine_schema
from app.v1.service import type_vaccine_service
from app.v1.utils import get_db
from app.v1.schema.user_schema import User
from app.v1.service.auth_service import get_current_user

router = APIRouter(prefix = '/api/v1/clinic')


@router.post (
    '/',
    tags = ['clinic'],
    status_code = status.HTTP_201_CREATED,
    response_model = type_vaccine_schema.TypeVaccine,
    dependencies = [Depends(get_db)]
)
def create_clinic (
    type_vaccine: type_vaccine_schema.TypeVaccineCreate = Body(...),
    current_user: User = Depends(get_current_user)):
    return type_vaccine_service.create_clinic(clinic, current_user)


@router.get (
    '/',
    tags = ['clinic'],
    status_code = status.HTTP_200_OK,
    response_model = List[type_vaccine_schema.TypeVaccine],
    dependencies = [Depends(get_db)]
)
def get_clinic(
    is_done: Optional[bool] = Query(None),
    current_user: User = Depends(get_current_user)
):
    return type_vaccine_service.get_clinics(current_user, is_done)


@router.get (
    '/{type_vaccine_id}',
    tags = ['clinic'],
    status_code = status.HTTP_200_OK,
    response_model = type_vaccine_schema.TypeVaccine,
    dependencies = [Depends(get_db)]
)
def get_clinic(
    type_vaccine_id: int = Path (
        ...,
        gt=0
    ),
    current_user: User = Depends(get_current_user)
):
    return type_vaccine_service.get_type_vaccine(type_vaccine_id, current_user)


@router.patch (
    '/{type_vaccine_id}/update',
    tags = ['clinic'],
    status_code = status.HTTP_200_OK,
    response_model = type_vaccine_schema.TypeVaccine,
    dependencies=[Depends(get_db)]
)
def type_vaccine_update (
    type_vaccine_id: int = Path(
        ...,
        gt=0
    ),
    current_user: User = Depends(get_current_user)
):
    return type_vaccine_service.update_status_task(type_vaccine_id, current_user)


@router.delete(
    "/{type_vaccine_id}/",
    tags=["clinic"],
    status_code=status.HTTP_200_OK,
    dependencies=[Depends(get_db)]
)
def delete_clinic(
    type_vaccine_id: int = Path(
        ...,
        gt=0
    ),
    current_user: User = Depends(get_current_user)
):
    type_vaccine_service.delete_clinic(type_vaccine_id, current_user)

    return {
        'msg': 'clinic has been deleted sucessfully'
    }
