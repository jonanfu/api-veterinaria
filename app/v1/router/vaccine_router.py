from fastapi import APIRouter, Depends, Body
from fastapi import status
from fastapi import Query
from fastapi import Path

from typing import List, Optional

from app.v1.schema import vaccine_schema
from app.v1.service import vaccine_service
from app.v1.utils import get_db
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
    vaccine: vaccine_schema.VaccineCreate = Body(...),
    current_user: User = Depends(get_current_user)):
    return vaccine_service.create_vaccine(vaccine, current_user)


@router.get (
    '/',
    tags = ['vaccine'],
    status_code = status.HTTP_200_OK,
    response_model = List[vaccine_schema.Vaccine],
    dependencies = [Depends(get_db)]
)
def get_vaccine(
    is_done: Optional[bool] = Query(None),
    current_user: User = Depends(get_current_user)
):
    return vaccine_service.get_vaccines(current_user, is_done)


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
    ),
    current_user: User = Depends(get_current_user)
):
    return vaccine_service.get_vaccine(vaccine_id, current_user)


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
    current_user: User = Depends(get_current_user)
):
    return vaccine_service.update_status_task(vaccine_id, current_user)


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
    ),
    current_user: User = Depends(get_current_user)
):
    vaccine_service.delete_vaccine(vaccine_id, current_user)

    return {
        'msg': 'vaccine has been deleted sucessfully'
    }
