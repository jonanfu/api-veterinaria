from fastapi import APIRouter, Depends, Body
from fastapi import status
from fastapi import Query
from fastapi import Path

from typing import List, Optional

from app.v1.schema import esthetic_has_type_service_schema
from app.v1.service import esthetic_has_type_service_service
from app.v1.utils.db import get_db
from app.v1.schema.user_schema import User
from app.v1.service.auth_service import get_current_user

router = APIRouter(prefix='/api/v1/esthetic-has-type-service')


@router.post(
    '/',
    tags=['esthetic-has-type-service'],
    status_code=status.HTTP_201_CREATED,
    response_model=esthetic_has_type_service_schema.EstheticHasTypeService,
    dependencies=[Depends(get_db)]
)
def create_esthetic_hast_type_service(
    esthetic_has_type_service: esthetic_has_type_service_schema.EstheticHasTypeServiceCreate = Body(
        ...)
):
    return esthetic_has_type_service_service.create_esthetic_hast_type_service(esthetic_has_type_service)


@router.get(
    '/',
    tags=['esthetic-has-type-service'],
    status_code=status.HTTP_200_OK,
    response_model=List[esthetic_has_type_service_schema.EstheticHasTypeService],
    dependencies=[Depends(get_db)]
)
def get_esthetic_hast_type_services():
    return esthetic_has_type_service_service.get_esthetic_hast_type_services()


@router.get(
    '/{esthetic_hast_type_service_id}',
    tags=['esthetic-has-type-service'],
    status_code=status.HTTP_200_OK,
    response_model=esthetic_has_type_service_schema.EstheticHasTypeService,
    dependencies=[Depends(get_db)]
)
def get_esthetic_hast_type_service(
    esthetic_has_type_service_id: int = Path(
        ...,
        gt=0
    )
):
    return esthetic_has_type_service_service.get_esthetic_has_type_service(esthetic_has_type_service_id)


@router.patch(
    '/{esthetic_has_type_service_id}/update',
    tags=['esthetic-has-type-service'],
    status_code=status.HTTP_200_OK,
    response_model=esthetic_has_type_service_schema.EstheticHasTypeService,
    dependencies=[Depends(get_db)]
)
def esthetic_has_type_service_update(
    esthetic_has_type_service_id: int = Path(
        ...,
        gt=0
    ),
    esthetic_has_type_service: esthetic_has_type_service_schema.EstheticHasTypeService = Body(
        ...)
):
    return esthetic_has_type_service_service.update_esthetic_has_type_service(esthetic_has_type_service_id,
                                                                              esthetic=esthetic_has_type_service.esthetic,
                                                                              type_service=esthetic_has_type_service.type_service
                                                                              )


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
    )
):
    esthetic_has_type_service_service.delete_esthetic_has_type_service(
        esthetic_has_type_service_id)

    return {
        'msg': 'esthetic has type service has been deleted sucessfully'
    }
