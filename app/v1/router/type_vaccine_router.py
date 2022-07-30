from fastapi import APIRouter, Depends, Body
from fastapi import status
from fastapi import Query
from fastapi import Path

from typing import List, Optional

from app.v1.schema import type_vaccine_schema
from app.v1.service import type_vaccine_service
from app.v1.utils.db import get_db
from app.v1.schema.user_schema import User
from app.v1.service.auth_service import get_current_user

router = APIRouter(prefix = '/api/v1/type_vaccine')


@router.post (
    '/',
    tags = ['type_vaccine'],
    status_code = status.HTTP_201_CREATED,
    response_model = type_vaccine_schema.TypeVaccine,
    dependencies = [Depends(get_db)]
)
def create_type_vaccine (
    type_vaccine: type_vaccine_schema.TypeVaccineCreate = Body(...)):
    return type_vaccine_service.create_type_vaccine(type_vaccine)


@router.get (
    '/',
    tags = ['type_vaccine'],
    status_code = status.HTTP_200_OK,
    response_model = List[type_vaccine_schema.TypeVaccine],
    dependencies = [Depends(get_db)]
)
def get_type_vaccine():
    return type_vaccine_service.get_type_vaccine()


@router.get (
    '/{type_vaccine_id}',
    tags = ['type_vaccine'],
    status_code = status.HTTP_200_OK,
    response_model = type_vaccine_schema.TypeVaccine,
    dependencies = [Depends(get_db)]
)
def get_type_vaccine(
    type_vaccine_id: int = Path (
        ...,
        gt=0
    )
):
    return type_vaccine_service.get_type_vaccine(type_vaccine_id)


@router.patch (
    '/{type_vaccine_id}/update',
    tags = ['type_vaccine'],
    status_code = status.HTTP_200_OK,
    response_model = type_vaccine_schema.TypeVaccine,
    dependencies=[Depends(get_db)]
)
def type_vaccine_update (
    type_vaccine_id: int = Path(
        ...,
        gt=0
    ),
    type_vaccine: type_vaccine_schema.TypeVaccine = Body(...)
):
    return type_vaccine_service.update_type_vaccine(type_vaccine_id,
        name = type_vaccine.name,
        description = type_vaccine.description
        ) 


@router.delete(
    "/{type_vaccine_id}/",
    tags=["type_vaccine"],
    status_code=status.HTTP_200_OK,
    dependencies=[Depends(get_db)]
)
def delete_type_vaccine(
    type_vaccine_id: int = Path(
        ...,
        gt=0
    )
):
    type_vaccine_service.delete_type_vaccine(type_vaccine_id)

    return {
        'msg': 'type_vaccine has been deleted sucessfully'
    }
