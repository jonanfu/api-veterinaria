from fastapi import APIRouter, Depends, Body
from fastapi import status
from fastapi import Query
from fastapi import Path

from typing import List, Optional

from app.v1.schema import esthetic_has_type_service_schema
from app.v1.service import esthetic_has_type_service_service
from app.v1.utils import get_db
from app.v1.schema.user_schema import User
from app.v1.service.auth_service import get_current_user

router = APIRouter(prefix = '/api/v1/esthetic-has-type-service')


@router.post (
    '/',
    tags = ['esthetic-has-type-service'],
    status_code = status.HTTP_201_CREATED,
    response_model = esthetic_has_type_service_schema.EstheticHasTypeService,
    dependencies = [Depends(get_db)]
)
def create_esthetic_hast_type_service (
    todo: esthetic_has_type_service_schema.EstheticHasTypeServiceCreate = Body(...),
    current_user: User = Depends(get_current_user)):
    return esthetic_has_type_service_service.create_esthetic_hast_type_service(esthetic_hast_type_service, current_user)


@router.get (
    '/',
    tags = ['esthetic-has-type-service'],
    status_code = status.HTTP_200_OK,
    response_model = List[esthetic_has_type_service_schema.EstheticHasTypeService],
    dependencies = [Depends(get_db)]
)
def get_esthetic_hast_type_service(
    is_done: Optional[bool] = Query(None),
    current_user: User = Depends(get_current_user)
):
    return esthetic_has_type_service_service.get_esthetic_hast_type_services(current_user, is_done)


@router.get (
    '/{esthetic_hast_type_service_id}',
    tags = ['esthetic-has-type-service'],
    status_code = status.HTTP_200_OK,
    response_model = esthetic_has_type_service_schema.EstheticHasTypeService,
    dependencies = [Depends(get_db)]
)
def get_esthetic_hast_type_service(
    esthetic_has_type_service_id: int = Path (
        ...,
        gt=0
    ),
    current_user: User = Depends(get_current_user)
):
    return esthetic_has_type_service_service.get_esthetic_has_type_service(esthetic_hast_type_service_id, current_user)


@router.patch (
    '/{esthetic_has_type_service_id}/update',
    tags = ['esthetic-has-type-service'],
    status_code = status.HTTP_200_OK,
    response_model = esthetic_has_type_service_schema.EstheticHasTypeService,
    dependencies=[Depends(get_db)]
)
def esthetic_has_type_service_update (
    esthetic_has_type_service_id: int = Path(
        ...,
        gt=0
    ),
    current_user: User = Depends(get_current_user)
):
    return esthetic_has_type_service_service.update_status_task(esthetic_has_type_service_id, current_user)


@router.delete(
    "/{esthetic_has_type_service_id}/",
    tags=["esthetic-has-type-service"],
    status_code=status.HTTP_200_OK,
    dependencies=[Depends(get_db)]
)
def delete_esthetic_has_type_service(
    esthetic_has_type_service_id: int = Path(
        ...,
        gt=0
    ),
    current_user: User = Depends(get_current_user)
):
    esthetic_has_type_service_service.delete_esthetic_hast_type_service(esthetic_has_type_service_id, current_user)

    return {
        'msg': 'esthetic has type service has been deleted sucessfully'
    }
