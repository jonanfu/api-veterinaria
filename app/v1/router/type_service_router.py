from fastapi import APIRouter, Depends, Body
from fastapi import status
from fastapi import Query
from fastapi import Path

from typing import List, Optional

from app.v1.schema import type_service_schema
from app.v1.service import type_service_service
from app.v1.utils.db import get_db
from app.v1.schema.user_schema import User
from app.v1.service.auth_service import get_current_user

router = APIRouter(prefix = '/api/v1/type_service')


@router.post (
    '/',
    tags = ['type_service'],
    status_code = status.HTTP_201_CREATED,
    response_model = type_service_schema.TypeService,
    dependencies = [Depends(get_db)]
)
def create_type_service (
    type_service: type_service_schema.TypeServiceCreate = Body(...)):
    return type_service_service.create_type_service(type_service)


@router.get (
    '/',
    tags = ['type_service'],
    status_code = status.HTTP_200_OK,
    response_model = List[type_service_schema.TypeService],
    dependencies = [Depends(get_db)]
)
def get_type_service():
    return type_service_service.get_type_service()


@router.get (
    '/{type_service_id}',
    tags = ['type_service'],
    status_code = status.HTTP_200_OK,
    response_model = type_service_schema.TypeService,
    dependencies = [Depends(get_db)]
)
def get_type_service(
    type_service_id: int = Path (
        ...,
        gt=0
    )
):
    return type_service_service.get_type_service(type_service_id)


@router.patch (
    '/{type_service_id}/update',
    tags = ['type_service'],
    status_code = status.HTTP_200_OK,
    response_model = type_service_schema.TypeService,
    dependencies=[Depends(get_db)]
)
def type_service_update (
    type_service_id: int = Path(
        ...,
        gt=0
    ),
    type_service: type_service_schema.TypeService = Body(...)
):
    return type_service_service.update_type_service(type_service_id,
        name = type_service.name,
        description = type_service.description
        ) 


@router.delete(
    "/{type_service_id}/",
    tags=["type_service"],
    status_code=status.HTTP_200_OK,
    dependencies=[Depends(get_db)]
)
def delete_type_service(
    type_service_id: int = Path(
        ...,
        gt=0
    )
):
    type_service_service.delete_type_service(type_service_id)

    return {
        'msg': 'type_service has been deleted sucessfully'
    }
