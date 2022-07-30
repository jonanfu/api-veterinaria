from fastapi import APIRouter, Depends, Body
from fastapi import status
from fastapi import Query
from fastapi import Path

from typing import List, Optional

from app.v1.schema import detail_purchase_schema
from app.v1.service import detail_purchase_service
from app.v1.utils.db import get_db
from app.v1.schema.user_schema import User
from app.v1.service.auth_service import get_current_user

router = APIRouter(prefix='/api/v1/detail-purchase')


@router.post(
    '/',
    tags=['detail-purchase'],
    status_code=status.HTTP_201_CREATED,
    response_model=detail_purchase_schema.DetailPurchase,
    dependencies=[Depends(get_db)]
)
def create_detail_purchase(
    detail_purchase: detail_purchase_schema.DetailPurchaseCreate = Body(...)
):
    return detail_purchase_service.create_detail_purchase(detail_purchase)


@router.get(
    '/',
    tags=['detail-purchase'],
    status_code=status.HTTP_200_OK,
    response_model=List[detail_purchase_schema.DetailPurchase],
    dependencies=[Depends(get_db)]
)
def get_detail_purchase():
    return detail_purchase_service.get_detail_purchases()


@router.get(
    '/{detail_purchase_id}',
    tags=['detail-purchase'],
    status_code=status.HTTP_200_OK,
    response_model=detail_purchase_schema.DetailPurchase,
    dependencies=[Depends(get_db)]
)
def get_detail_purchase(
    detail_purchase_id: int = Path(
        ...,
        gt=0
    )
):
    return detail_purchase_service.get_detail_purchase(detail_purchase_id)


@router.patch(
    '/{detail_purchase_id}/update',
    tags=['detail-purchase'],
    status_code=status.HTTP_200_OK,
    response_model=detail_purchase_schema.DetailPurchase,
    dependencies=[Depends(get_db)]
)
def detail_purchase_update(
    detail_purchase_id: int = Path(
        ...,
        gt=0
    ),
    detail_purchase: detail_purchase_schema.DetailPurchase = Body(...)
):
    return detail_purchase_service.update_detail_purchase(detail_purchase_id,
                                                          amount=detail_purchase.amount,
                                                          price=detail_purchase.price,
                                                          tax=detail_purchase.tax,
                                                          subtotal=detail_purchase.profit_percentage,
                                                          purchase=detail_purchase.purchase,
                                                          product=detail_purchase.product
                                                          )


@router.delete(
    "/{detail_purchase_id}/",
    tags=["detail-purchase"],
    status_code=status.HTTP_200_OK,
    dependencies=[Depends(get_db)]
)
def delete_detail_purchase(
    detail_purchase_id: int = Path(
        ...,
        gt=0
    )
):
    detail_purchase_service.delete_detail_purchase(detail_purchase_id)

    return {
        'msg': 'detail purchase has been deleted sucessfully'
    }
