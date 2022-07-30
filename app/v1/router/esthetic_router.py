from fastapi import APIRouter, Depends, Body
from fastapi import status
from fastapi import Query
from fastapi import Path

from typing import List, Optional

from app.v1.schema import esthetic_has_type_service_schema, esthetic_schema
from app.v1.service import esthetic_service
from app.v1.utils.db import get_db
from app.v1.schema.user_schema import User
from app.v1.service.auth_service import get_current_user

router = APIRouter(prefix = '/api/v1/esthetic')


@router.post (
    '/',
    tags = ['esthetic'],
    status_code = status.HTTP_201_CREATED,
    response_model = esthetic_schema.Esthetic,
    dependencies = [Depends(get_db)]
)
def create_esthetic (
    esthetic: esthetic_schema.EstheticCreate = Body(...)
):
    return esthetic_service.create_esthetic(esthetic)


@router.get (
    '/',
    tags = ['esthetic'],
    status_code = status.HTTP_200_OK,
    response_model = List[esthetic_schema.Esthetic],
    dependencies = [Depends(get_db)]
)
def get_esthetic():
    return esthetic_service.get_esthetics()


@router.get (
    '/{esthetic_id}',
    tags = ['esthetic'],
    status_code = status.HTTP_200_OK,
    response_model = esthetic_schema.Esthetic,
    dependencies = [Depends(get_db)]
)
def get_esthetic(
    esthetic_id: int = Path (
        ...,
        gt=0
    )
):
    return esthetic_service.get_esthetic(esthetic_id)


@router.patch (
    '/{esthetic_id}/update',
    tags = ['esthetic'],
    status_code = status.HTTP_200_OK,
    response_model = esthetic_schema.Esthetic,
    dependencies=[Depends(get_db)]
)
def esthetic_update (
    esthetic_id: int = Path(
        ...,
        gt=0
    ),
    esthetic_has_type_service: esthetic_has_type_service_schema.EstheticHasTypeService = Body(...)
):
    return esthetic_service.update_esthetic(esthetic_id,
        date=esthetic_has_type_service.date,
        hour = esthetic_has_type_service.hour,
        activate_notification=esthetic_has_type_service.activate_notification,
        price=esthetic_has_type_service.price,
        form_payment=esthetic_has_type_service.form_payment,
        is_paid=esthetic_has_type_service.is_paid,
        patient=esthetic_has_type_service.patient
    )


@router.delete(
    "/{esthetic_id}/",
    tags=["esthetic"],
    status_code=status.HTTP_200_OK,
    dependencies=[Depends(get_db)]
)
def delete_esthetic(
    esthetic_id: int = Path(
        ...,
        gt=0
    )
):
    esthetic_service.delete_esthetic(esthetic_id)

    return {
        'msg': 'esthetic has been deleted sucessfully'
    }
