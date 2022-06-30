from fastapi import APIRouter, Depends, Body
from fastapi import status
from fastapi import Query
from fastapi import Path

from typing import List, Optional

from app.v1.schema import hospitalization_schema
from app.v1.service import hospitalization_service
from app.v1.schema import patient_schema
from app.v1.utils import get_db
from app.v1.schema.user_schema import User
from app.v1.service.auth_service import get_current_user

router = APIRouter(prefix = '/api/v1/hospitalization')


@router.post (
    '/',
    tags = ['hospitalization'],
    status_code = status.HTTP_201_CREATED,
    response_model = hospitalization_schema.Hospitalization,
    dependencies = [Depends(get_db)]
)
def create_hospitalization (
    hospitalization: hospitalization_schema.HospitalizationCreate = Body(...),
    current_user: User = Depends(get_current_user)):
    return hospitalization_service.create_hospitalization(hospitalization, current_user)


@router.get (
    '/',
    tags = ['hospitalization'],
    status_code = status.HTTP_200_OK,
    response_model = List[hospitalization_schema.Hospitalization],
    dependencies = [Depends(get_db)]
)
def get_hospitalization(
    is_done: Optional[bool] = Query(None),
    current_user: User = Depends(get_current_user)
):
    return hospitalization_service.get_hospitalizations(current_user, is_done)


@router.get (
    '/{hospitalization_id}',
    tags = ['hospitalization'],
    status_code = status.HTTP_200_OK,
    response_model = hospitalization_schema.Hospitalization,
    dependencies = [Depends(get_db)]
)
def get_hospitalization(
    hospitalization_id: int = Path (
        ...,
        gt=0
    ),
    current_user: User = Depends(get_current_user)
):
    return hospitalization_service.get_task(hospitalization_id, current_user)


@router.patch (
    '/{hospitalization_id}/update',
    tags = ['hospitalization'],
    status_code = status.HTTP_200_OK,
    response_model = hospitalization_schema.Hospitalization,
    dependencies=[Depends(get_db)]
)
def hospitalization_update (
    hospitalization_id: int = Path(
        ...,
        gt=0
    ),
    current_user: User = Depends(get_current_user)
):
    return hospitalization_service.update_status_task(hospitalization_id, current_user)


@router.delete(
    "/{hospitalization_id}/",
    tags=["hospitalization"],
    status_code=status.HTTP_200_OK,
    dependencies=[Depends(get_db)]
)
def delete_hospitalization(
    hospitalization_id: int = Path(
        ...,
        gt=0
    ),
    current_user: User = Depends(get_current_user)
):
    hospitalization_service.delete_hospitalization(hospitalization_id, current_user)

    return {
        'msg': 'hospitalization has been deleted sucessfully'
    }
