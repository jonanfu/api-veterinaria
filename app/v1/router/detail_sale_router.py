from fastapi import APIRouter, Depends, Body
from fastapi import status
from fastapi import Query
from fastapi import Path

from typing import List, Optional

from app.v1.schema import detail_sale_schema
from app.v1.service import detail_sale_service
from app.v1.utils.db import get_db
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
    detail_sale: detail_sale_schema.DetailSaleCreate = Body(...),
    ):
    return detail_sale_service.create_detail_clinic(detail_sale)


@router.get (
    '/',
    tags = ['detail-sale'],
    status_code = status.HTTP_200_OK,
    response_model = List[detail_sale_schema.DetailSale],
    dependencies = [Depends(get_db)]
)
def get_clinic():
    return detail_sale_service.get_detail_sales()


@router.get (
    '/{detail_sale_id}',
    tags = ['detail-sale'],
    status_code = status.HTTP_200_OK,
    response_model = detail_sale_schema.DetailSale,
    dependencies = [Depends(get_db)]
)
def get_detail_sale(
    detail_sale_id: int = Path (
        ...,
        gt=0
    )
):
    return detail_sale_service.get_detail_sale(detail_sale_id)


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
    detail_sale: detail_sale_schema.DetailSale = Body(...)
):
    return detail_sale_service.update_detail_sale(detail_sale_id,
        amount=detail_sale.amount,
        price=detail_sale.price,
        tax=detail_sale.tax,
        subtotal=detail_sale.subtotal,
        discount=detail_sale.discount,
        sale=detail_sale.sale,
        product=detail_sale.product
    )


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
    )
):
    detail_sale_service.delete_clinic(detail_sale_id)

    return {
        'msg': 'detail sale has been deleted sucessfully'
    }
