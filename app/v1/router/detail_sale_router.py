from fastapi import APIRouter, Depends, Body
from fastapi import status
from fastapi import Query
from fastapi import Path

from typing import List, Optional

from app.v1.schema import detail_sale_schema
from app.v1.schema import sale_schema
from app.v1.schema import product
from app.v1.service import detail_sale_service
from app.v1.utils import get_db
from app.v1.schema.user_schema import User
from app.v1.service.auth_service import get_current_user

router = APIRouter(prefix = '/api/v1/detail-sale')


@router.post (
    '/',
    tags = ['detail-sale'],
    status_code = status.HTTP_201_CREATED,
    response_model = detail_sale_schema.DetailSale,
    dependencies = [Depends(get_db)]
)
def create_detail_sale (
    todo: detail_sale_schema.DetailSaleCreate = Body(...),
    current_user: User = Depends(get_current_user)):
    return detail_sale_service.create_detail_clinic(detail_sale, current_user)


@router.get (
    '/',
    tags = ['detail-sale'],
    status_code = status.HTTP_200_OK,
    response_model = List[detail_sale_schema.Detail_sale],
    dependencies = [Depends(get_db)]
)
def get_clinic(
    is_done: Optional[bool] = Query(None),
    current_user: User = Depends(get_current_user)
):
    return detail_sale_service.get_detail_sales(current_user, is_done)


@router.get (
    '/{detail_sale_id}',
    tags = ['detail-sale'],
    status_code = status.HTTP_200_OK,
    response_model = detail_sale_schema.detail_sale,
    dependencies = [Depends(get_db)]
)
def get_detail_sale(
    detail_sale_id: int = Path (
        ...,
        gt=0
    ),
    current_user: User = Depends(get_current_user)
):
    return detail_sale_service.get_task(detail_sale_id, current_user)


@router.patch (
    '/{detail_sale_id}/update',
    tags = ['detail-sale'],
    status_code = status.HTTP_200_OK,
    response_model = detail_sale_schema.DetailSale,
    dependencies=[Depends(get_db)]
)
def detail_sale_update (
    detail_sale_id: int = Path(
        ...,
        gt=0
    ),
    current_user: User = Depends(get_current_user)
):
    return detail_sale_service.update_detail_service(detail_sale_id, current_user)


@router.delete(
    "/{detail_sale_id}/",
    tags=["detail-sale"],
    status_code=status.HTTP_200_OK,
    dependencies=[Depends(get_db)]
)
def delete_detail_sale(
    detail_sale_id: int = Path(
        ...,
        gt=0
    ),
    current_user: User = Depends(get_current_user)
):
    detail_sale_service.delete_clinic(detail_sale_id, current_user)

    return {
        'msg': 'detail sale has been deleted sucessfully'
    }
