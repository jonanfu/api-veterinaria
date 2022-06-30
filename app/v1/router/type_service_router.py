from fastapi import APIRouter, Depends, Body
from fastapi import status
from fastapi import Query
from fastapi import Path

from typing import List, Optional

from app.v1.schema import type_service_schema
from app.v1.service import type_service_service
from app.v1.utils import get_db
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
    type_service: type_service_schema.TypeServiceCreate = Body(...),
    current_user: User = Depends(get_current_user)):
    return type_service_service.create_type_service(type_service, current_user)


@router.get (
    '/',
    tags = ['type_service'],
    status_code = status.HTTP_200_OK,
    response_model = List[type_service_schema.TypeService],
    dependencies = [Depends(get_db)]
)
def get_type_service(
    is_done: Optional[bool] = Query(None),
    current_user: User = Depends(get_current_user)
):
    return type_service_service.get_type_services(current_user, is_done)


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
    ),
    current_user: User = Depends(get_current_user)
):
    return type_service_service.get_type_service(type_service_id, current_user)


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
    current_user: User = Depends(get_current_user)
):
    return type_service_service.update_status_task(type_service_id, current_user)


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
    ),
    current_user: User = Depends(get_current_user)
):
    type_service_service.delete_type_service(type_service_id, current_user)

    return {
        'msg': 'type service has been deleted sucessfully'
    }
