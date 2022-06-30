from fastapi import APIRouter, Depends, Body
from fastapi import status
from fastapi import Query
from fastapi import Path

from typing import List, Optional

from app.v1.schema import pet_daycare_schema
from app.v1.schema import patient_schema
from app.v1.service import pet_daycare_service
from app.v1.utils import get_db
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
    pet_daycare: pet_daycare_schema.PetDaycareCreate = Body(...),
    current_user: User = Depends(get_current_user)):
    return pet_daycare_service.create_pet_daycare(pet_daycare, current_user)


@router.get (
    '/',
    tags = ['pet_daycare'],
    status_code = status.HTTP_200_OK,
    response_model = List[pet_daycare_schema.PetDaycare],
    dependencies = [Depends(get_db)]
)
def get_pet_daycare(
    is_done: Optional[bool] = Query(None),
    current_user: User = Depends(get_current_user)
):
    return pet_daycare_service.get_pet_daycares(current_user, is_done)


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
    ),
    current_user: User = Depends(get_current_user)
):
    return pet_daycare_service.get_task(pet_daycare_id, current_user)


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
    current_user: User = Depends(get_current_user)
):
    return pet_daycare_service.update_pet_daycare(pet_daycare_id, current_user)


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
    ),
    current_user: User = Depends(get_current_user)
):
    pet_daycare_service.delete_pet_daycare(pet_daycare_id, current_user)

    return {
        'msg': 'pet daycare has been deleted sucessfully'
    }
