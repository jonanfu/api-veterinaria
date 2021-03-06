from fastapi import APIRouter, Depends, Body
from fastapi import status
from fastapi import Query
from fastapi import Path

from typing import List, Optional

from app.v1.schema import laboratory_schema
from app.v1.service import laboratory_service
from app.v1.utils.db import get_db
from app.v1.schema.user_schema import User
from app.v1.service.auth_service import get_current_user

router = APIRouter(prefix = '/api/v1/laboratory')


@router.post (
    '/',
    tags = ['laboratory'],
    status_code = status.HTTP_201_CREATED,
    response_model = laboratory_schema.Laboratory,
    dependencies = [Depends(get_db)]
)
def create_laboratory (
    laboratory: laboratory_schema.LaboratoryCreate = Body(...)
    ):
    return laboratory_service.create_laboratory(laboratory)


@router.get (
    '/',
    tags = ['laboratory'],
    status_code = status.HTTP_200_OK,
    response_model = List[laboratory_schema.Laboratory],
    dependencies = [Depends(get_db)]
)
def get_laboratory():
    return laboratory_service.get_laboratorys()


@router.get (
    '/{laboratory_id}',
    tags = ['laboratory'],
    status_code = status.HTTP_200_OK,
    response_model = laboratory_schema.Laboratory,
    dependencies = [Depends(get_db)]
)
def get_laboratory(
    laboratory_id: int = Path (
        ...,
        gt=0
    )
):
    return laboratory_service.get_task(laboratory_id)


@router.patch (
    '/{laboratory_id}/update',
    tags = ['laboratory'],
    status_code = status.HTTP_200_OK,
    response_model = laboratory_schema.Laboratory,
    dependencies=[Depends(get_db)]
)
def laboratory_update (
    laboratory_id: int = Path(
        ...,
        gt=0
    ),
    laboratory: laboratory_schema.Laboratory = Body(...)
):
    return laboratory_service.update_laboratory(laboratory_id,
        name = laboratory.name,
        description = laboratory.description)


@router.delete(
    "/{laboratory_id}/",
    tags=["laboratory"],
    status_code=status.HTTP_200_OK,
    dependencies=[Depends(get_db)]
)
def delete_laboratory(
    laboratory_id: int = Path(
        ...,
        gt=0
    )
):
    laboratory_service.delete_laboratory(laboratory_id)

    return {
        'msg': 'laboratory has been deleted sucessfully'
    }
