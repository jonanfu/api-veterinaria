from fastapi import APIRouter, Depends, Body
from fastapi import status
from fastapi import Query
from fastapi import Path

from typing import List, Optional

from app.v1.schema import type_dewormer_schema
from app.v1.service import type_dewormer_service
from app.v1.utils import get_db
from app.v1.schema.user_schema import User
from app.v1.service.auth_service import get_current_user

router = APIRouter(prefix = '/api/v1/type_dewormer')


@router.post (
    '/',
    tags = ['type_dewormer'],
    status_code = status.HTTP_201_CREATED,
    response_model = type_dewormer_schema.TypeDewormer,
    dependencies = [Depends(get_db)]
)
def create_type_dewormer (
    todo: type_dewormer_schema.TypeDewormerCreate = Body(...),
    current_user: User = Depends(get_current_user)):
    return type_dewormer_service.create_type_dewormer(type_dewormer, current_user)


@router.get (
    '/',
    tags = ['type_dewormer'],
    status_code = status.HTTP_200_OK,
    response_model = List[type_dewormer_schema.TypeDewormer],
    dependencies = [Depends(get_db)]
)
def get_type_dewormer(
    is_done: Optional[bool] = Query(None),
    current_user: User = Depends(get_current_user)
):
    return type_dewormer_service.get_type_dewormers(current_user, is_done)


@router.get (
    '/{type_dewormer_id}',
    tags = ['type_dewormer'],
    status_code = status.HTTP_200_OK,
    response_model = type_dewormer_schema.TypeDewormer,
    dependencies = [Depends(get_db)]
)
def get_type_dewormer(
    type_dewormer_id: int = Path (
        ...,
        gt=0
    ),
    current_user: User = Depends(get_current_user)
):
    return type_dewormer_service.get_type_dewormer(type_dewormer_id, current_user)


@router.patch (
    '/{type_dewormer_id}/update',
    tags = ['type_dewormer'],
    status_code = status.HTTP_200_OK,
    response_model = type_dewormer_schema.TypeDewormer,
    dependencies=[Depends(get_db)]
)
def type_dewormer_update (
    type_dewormer_id: int = Path(
        ...,
        gt=0
    ),
    current_user: User = Depends(get_current_user)
):
    return type_dewormer_service.update_status_task(type_dewormer_id, current_user)


@router.delete(
    "/{type_dewormer_id}/",
    tags=["type_dewormer"],
    status_code=status.HTTP_200_OK,
    dependencies=[Depends(get_db)]
)
def delete_type_dewormer(
    type_dewormer_id: int = Path(
        ...,
        gt=0
    ),
    current_user: User = Depends(get_current_user)
):
    type_dewormer_service.delete_type_dewormer(type_dewormer_id, current_user)

    return {
        'msg': 'type dewormer has been deleted sucessfully'
    }
