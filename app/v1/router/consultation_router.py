from fastapi import APIRouter, Depends, Body
from fastapi import status
from fastapi import Query
from fastapi import Path

from typing import List, Optional

from app.v1.schema import consultation_schema
from app.v1.schema import vaccine_schema
from app.v1.schema import dewormer_schema
from app.v1.service import consultation_service
from app.v1.utils import get_db
from app.v1.schema.user_schema import User
from app.v1.service.auth_service import get_current_user

router = APIRouter(prefix = '/api/v1/consultation')


@router.post (
    '/',
    tags = ['consultation'],
    status_code = status.HTTP_201_CREATED,
    response_model = consultation_schema.Clinic,
    dependencies = [Depends(get_db)]
)
def create_consultaion (
    todo: consultation_schema.ClinicCreate = Body(...),
    current_user: User = Depends(get_current_user)):
    return consultation_service.create_consultation(consultation, current_user)


@router.get (
    '/',
    tags = ['consultation'],
    status_code = status.HTTP_200_OK,
    response_model = List[consultation_schema.Consultation],
    dependencies = [Depends(get_db)]
)
def get_consultation(
    is_done: Optional[bool] = Query(None),
    current_user: User = Depends(get_current_user)
):
    return consultation_service.get_consultation(current_user, is_done)


@router.get (
    '/{consultation_id}',
    tags = ['consultation'],
    status_code = status.HTTP_200_OK,
    response_model = consultation_schema.Consultation,
    dependencies = [Depends(get_db)]
)
def get_consultation(
    consultation_id: int = Path (
        ...,
        gt=0
    ),
    current_user: User = Depends(get_current_user)
):
    return consultation_service.get_consultation(consultation_id, current_user)


@router.patch (
    '/{consultation_id}/update',
    tags = ['consultation'],
    status_code = status.HTTP_200_OK,
    response_model = consultation_schema.Consultation,
    dependencies=[Depends(get_db)]
)
def consultation_update (
    task_id: int = Path(
        ...,
        gt=0
    ),
    current_user: User = Depends(get_current_user)
):
    return consultation_service.update_status_task(consultation_id, current_user)



@router.delete(
    "/{consultation_id}/",
    tags=["consultation"],
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
    consultation_service.delete_consultation(consultation_id, current_user)

    return {
        'msg': 'consultation has been deleted sucessfully'
    }
