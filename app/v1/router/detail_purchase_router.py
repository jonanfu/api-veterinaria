from fastapi import APIRouter, Depends, Body
from fastapi import status
from fastapi import Query
from fastapi import Path

from typing import List, Optional

from app.v1.schema import detail_purchase_schema
from app.v1.service import detail_purchase_service
from app.v1.schema import purchase_schema
from app.v1.schema import product_schema
from app.v1.utils import get_db
from app.v1.schema.user_schema import User
from app.v1.service.auth_service import get_current_user

router = APIRouter(prefix = '/api/v1/detail-purchase')


@router.post (
    '/',
    tags = ['detail-purchase'],
    status_code = status.HTTP_201_CREATED,
    response_model = detail_purchase_schema.DetailPurchase,
    dependencies = [Depends(get_db)]
)
def create_detail_purchase (
    detail_purchsase: detail_purchase_schema.DetailPurchaseCreate = Body(...),
    current_user: User = Depends(get_current_user)):
    return detail_purchase_service.create_detail_purchase(detail_purchase, current_user)


@router.get (
    '/',
    tags = ['detail-purchase'],
    status_code = status.HTTP_200_OK,
    response_model = List[detail_purchase_schema.Clinic],
    dependencies = [Depends(get_db)]
)
def get_detail_purchase(
    is_done: Optional[bool] = Query(None),
    current_user: User = Depends(get_current_user)
):
    return detail_purchase_service.get_clinics(current_user, is_done)


@router.get (
    '/{detail_clinic_id}',
    tags = ['detail-purchase'],
    status_code = status.HTTP_200_OK,
    response_model = detail_purchase_schema.DetailPurchase,
    dependencies = [Depends(get_db)]
)
def get_detail_purchase(
    task_id: int = Path (
        ...,
        gt=0
    ),
    current_user: User = Depends(get_current_user)
):
    return detail_purchase_service.get_task(detail_purchase_id, current_user)


@router.patch (
    '/{detail_purchase_id}/update',
    tags = ['detail-purchase'],
    status_code = status.HTTP_200_OK,
    response_model = detail_purchase_schema.DetailPurchase,
    dependencies=[Depends(get_db)]
)
def detail_purchase_update (
    detail_purchase_id: int = Path(
        ...,
        gt=0
    ),
    current_user: User = Depends(get_current_user)
):
    return detail_purchase_service.update_detail_purchase(detail_purchase_id, current_user)


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
    ),
    current_user: User = Depends(get_current_user)
):
    detail_purchase_service.delete_detail_purchase(detail_purchase_id, current_user)

    return {
        'msg': 'detail purchase has been deleted sucessfully'
    }
