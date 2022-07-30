from fastapi import APIRouter, Depends, Body
from fastapi import status
from fastapi import Query
from fastapi import Path

from typing import List, Optional

from app.v1.schema import type_dewormer_schema
from app.v1.service import type_dewormer_service
from app.v1.utils.db import get_db
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
    type_dewormer: type_dewormer_schema.TypeDewormerCreate = Body(...)):
    return type_dewormer_service.create_type_dewormer(type_dewormer)


@router.get (
    '/',
    tags = ['type_dewormer'],
    status_code = status.HTTP_200_OK,
    response_model = List[type_dewormer_schema.TypeDewormer],
    dependencies = [Depends(get_db)]
)
def get_type_dewormer():
    return type_dewormer_service.get_type_dewormer()


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
    )
):
    return type_dewormer_service.get_type_dewormer(type_dewormer_id)


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
    type_dewormer: type_dewormer_schema.TypeDewormer = Body(...)
):
    return type_dewormer_service.update_type_dewormer(type_dewormer_id,
        name = type_dewormer.name,
        description = type_dewormer.description
        ) 


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
    )
):
    type_dewormer_service.delete_type_dewormer(type_dewormer_id)

    return {
        'msg': 'type_dewormer has been deleted sucessfully'
    }
