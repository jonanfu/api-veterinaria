from fastapi import APIRouter, Depends, Body
from fastapi import status
from fastapi import Query
from fastapi import Path

from typing import List, Optional

from app.v1.schema import vaccine_schema
from app.v1.service import vaccine_service
from app.v1.utils.db import get_db
from app.v1.schema.user_schema import User
from app.v1.service.auth_service import get_current_user

router = APIRouter(prefix = '/api/v1/vaccine')


@router.post (
    '/',
    tags = ['vaccine'],
    status_code = status.HTTP_201_CREATED,
    response_model = vaccine_schema.Vaccine,
    dependencies = [Depends(get_db)]
)
def create_vaccine (
    vaccine: vaccine_schema.VaccineCreate = Body(...)
):
    return vaccine_service.create_vaccine(vaccine)


@router.get (
    '/',
    tags = ['vaccine'],
    status_code = status.HTTP_200_OK,
    response_model = List[vaccine_schema.Vaccine],
    dependencies = [Depends(get_db)]
)
def get_vaccines():
    return vaccine_service.get_vaccines()


@router.get (
    '/{vaccine_id}',
    tags = ['vaccine'],
    status_code = status.HTTP_200_OK,
    response_model = vaccine_schema.Vaccine,
    dependencies = [Depends(get_db)]
)
def get_vaccine(
    vaccine_id: int = Path (
        ...,
        gt=0
    )
):
    return vaccine_service.get_vaccine(vaccine_id)


@router.patch (
    '/{vaccine_id}/update',
    tags = ['vaccine'],
    status_code = status.HTTP_200_OK,
    response_model = vaccine_schema.Vaccine,
    dependencies=[Depends(get_db)]
)
def vaccine_update (
    vaccine_id: int = Path(
        ...,
        gt=0
    ),
    vaccine: vaccine_schema.Vaccine = Body(...)
):
    return vaccine_service.update_vaccine(vaccine_id,
        date= vaccine.date,
        lot= vaccine.lot,
        apply_vaccine= vaccine.apply_vaccine,
        expiration= vaccine.expiration,
        price= vaccine.price,
        weight= vaccine.weight,
        previous_vaccinations= vaccine.previous_vaccinations,
        type_vaccine= vaccine.type_vaccine
    )


@router.delete(
    "/{vaccine_id}/",
    tags=["vaccine"],
    status_code=status.HTTP_200_OK,
    dependencies=[Depends(get_db)]
)
def delete_vaccine(
    vaccine_id: int = Path(
        ...,
        gt=0
    )
):
    vaccine_service.delete_vaccine(vaccine_id)

    return {
        'msg': 'vaccine has been deleted sucessfully'
    }
