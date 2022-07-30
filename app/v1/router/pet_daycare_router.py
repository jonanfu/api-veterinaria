from fastapi import APIRouter, Depends, Body
from fastapi import status
from fastapi import Query
from fastapi import Path

from typing import List, Optional

from app.v1.schema import pet_daycare_schema
from app.v1.schema import patient_schema
from app.v1.service import pet_daycare_service
from app.v1.utils.db import get_db
from app.v1.schema.user_schema import User
from app.v1.service.auth_service import get_current_user

router = APIRouter(prefix = '/api/v1/pet-daycare')


@router.post (
    '/',
    tags = ['pet_daycare'],
    status_code = status.HTTP_201_CREATED,
    response_model = pet_daycare_schema.PetDaycare,
    dependencies = [Depends(get_db)]
)
def create_pet_daycare (
    pet_daycare: pet_daycare_schema.PetDaycareCreate = Body(...)
):
    return pet_daycare_service.create_pet_daycare(pet_daycare)


@router.get (
    '/',
    tags = ['pet_daycare'],
    status_code = status.HTTP_200_OK,
    response_model = List[pet_daycare_schema.PetDaycare],
    dependencies = [Depends(get_db)]
)
def get_pet_daycare():
    return pet_daycare_service.get_pet_daycares()


@router.get (
    '/{pet_daycare_id}',
    tags = ['pet_daycare'],
    status_code = status.HTTP_200_OK,
    response_model = pet_daycare_schema.PetDaycare,
    dependencies = [Depends(get_db)]
)
def get_pet_daycare(
    pet_daycare_id: int = Path (
        ...,
        gt=0
    )
):
    return pet_daycare_service.get_pet_daycare(pet_daycare_id)


@router.patch (
    '/{pet_daycare_id}/update',
    tags = ['pet_daycare'],
    status_code = status.HTTP_200_OK,
    response_model = pet_daycare_schema.PetDaycare,
    dependencies=[Depends(get_db)]
)
def pet_daycare_update (
    pet_daycare_id: int = Path(
        ...,
        gt=0
    ),
    pet_daycare: pet_daycare_schema.PetDaycare = Body(...)
):
    return pet_daycare_service.update_pet_daycare(pet_daycare_id,
        time_eat=pet_daycare.time_eat,
        notes=pet_daycare.notes,
        departure_date=pet_daycare.departure_date,
        moment_payment=pet_daycare.moment_payment,
        price=pet_daycare.price,
        form_payment=pet_daycare.form_payment,
        is_paid=pet_daycare.is_paid,
        patient=pet_daycare.patient
    )


@router.delete(
    "/{pet_daycare_id}/",
    tags=["pet_daycare"],
    status_code=status.HTTP_200_OK,
    dependencies=[Depends(get_db)]
)
def delete_pet_daycare(
    pet_daycare_id: int = Path(
        ...,
        gt=0
    )
):
    pet_daycare_service.delete_pet_daycare(pet_daycare_id)

    return {
        'msg': 'pet daycare has been deleted sucessfully'
    }
