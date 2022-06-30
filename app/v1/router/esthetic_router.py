from fastapi import APIRouter, Depends, Body
from fastapi import status
from fastapi import Query
from fastapi import Path

from typing import List, Optional

from app.v1.schema import esthetic_schema
from app.v1.service import esthetic_service
from app.v1.utils import get_db
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
    todo: esthetic_schema.EstheticCreate = Body(...),
    current_user: User = Depends(get_current_user)):
    return esthetic_service.create_esthetic(esthetic, current_user)


@router.get (
    '/',
    tags = ['esthetic'],
    status_code = status.HTTP_200_OK,
    response_model = List[esthetic_schema.Esthetic],
    dependencies = [Depends(get_db)]
)
def get_esthetic(
    is_done: Optional[bool] = Query(None),
    current_user: User = Depends(get_current_user)
):
    return esthetic_service.get_esthetics(current_user, is_done)


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
    ),
    current_user: User = Depends(get_current_user)
):
    return esthetic_service.get_esthetic(esthetic_id, current_user)


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
    current_user: User = Depends(get_current_user)
):
    return esthetic_service.update_esthetic(esthetic_id, current_user)


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
    ),
    current_user: User = Depends(get_current_user)
):
    esthetic_service.delete_esthetic(esthetic_id, current_user)

    return {
        'msg': 'esthetic has been deleted sucessfully'
    }
