from fastapi import APIRouter, Depends, Body
from fastapi import status
from fastapi import Query
from fastapi import Path

from typing import List, Optional

from app.v1.schema import dewormer_schema
from app.v1.service import dewormer_service
from app.v1.utils.db import get_db
from app.v1.schema.user_schema import User
from app.v1.service.auth_service import get_current_user

router = APIRouter(prefix = '/api/v1/dewormer')


@router.post (
    '/',
    tags = ['dewormer'],
    status_code = status.HTTP_201_CREATED,
    response_model = dewormer_schema.Dewormer,
    dependencies = [Depends(get_db)]
)
def create_dewormer (
    current_user: User = Depends(get_current_user)):
    return dewormer_service.create_dewormer(dewormer, current_user)


@router.get (
    '/',
    tags = ['dewormer'],
    status_code = status.HTTP_200_OK,
    response_model = List[dewormer_schema.Dewormer],
    dependencies = [Depends(get_db)]
)
def get_dewormer(
    is_done: Optional[bool] = Query(None),
    current_user: User = Depends(get_current_user)
):
    return dewormer_service.get_dewormers(current_user, is_done)


@router.get (
    '/{dewormer_id}',
    tags = ['dewormer'],
    status_code = status.HTTP_200_OK,
    response_model = dewormer_schema.Dewormer,
    dependencies = [Depends(get_db)]
)
def get_dewormer(
    dewormer_id: int = Path (
        ...,
        gt=0
    ),
    current_user: User = Depends(get_current_user)
):
    return dewormer_service.get_dewormer(dewormer_id, current_user)


@router.patch (
    '/{dewormer_id}/update',
    tags = ['dewormer'],
    status_code = status.HTTP_200_OK,
    response_model = dewormer_schema.Dewormer,
    dependencies=[Depends(get_db)]
)
def dewormer_update (
    dewormer_id: int = Path(
        ...,
        gt=0
    ),
    current_user: User = Depends(get_current_user)
):
    return dewormer_service.update_status_task(dewormer_id, current_user)


@router.delete(
    "/{dewormer_id}/",
    tags=["dewormer"],
    status_code=status.HTTP_200_OK,
    dependencies=[Depends(get_db)]
)
def delete_dewormer(
    dewormer_id: int = Path(
        ...,
        gt=0
    ),
    current_user: User = Depends(get_current_user)
):
    dewormer_service.delete_dewormer(dewormer_id, current_user)

    return {
        'msg': 'dewormer has been deleted sucessfully'
    }
