from fastapi import APIRouter, Depends, Body
from fastapi import status
from fastapi import Query
from fastapi import Path

from typing import List, Optional

from app.v1.schema import purchase_schema
from app.v1.service import purchase_service
from app.v1.utils import get_db
from app.v1.schema.user_schema import User
from app.v1.service.auth_service import get_current_user

router = APIRouter(prefix = '/api/v1/purchase')


@router.post (
    '/',
    tags = ['purchase'],
    status_code = status.HTTP_201_CREATED,
    response_model = purchase_schema.Purchase,
    dependencies = [Depends(get_db)]
)
def create_purchase (
    purchase: purchase_schema.PurchaseCreate = Body(...),
    current_user: User = Depends(get_current_user)):
    return purchase_service.create_purchase(purchase, current_user)


@router.get (
    '/',
    tags = ['purchase'],
    status_code = status.HTTP_200_OK,
    response_model = List[purchase_schema.Purchase],
    dependencies = [Depends(get_db)]
)
def get_purchase(
    is_done: Optional[bool] = Query(None),
    current_user: User = Depends(get_current_user)
):
    return purchase_service.get_purchases(current_user, is_done)


@router.get (
    '/{purchase_id}',
    tags = ['purchase'],
    status_code = status.HTTP_200_OK,
    response_model = purchase_schema.Purchase,
    dependencies = [Depends(get_db)]
)
def get_purchase(
    purchase_id: int = Path (
        ...,
        gt=0
    ),
    current_user: User = Depends(get_current_user)
):
    return purchase_service.get_task(purchase_id, current_user)


@router.patch (
    '/{purchase_id}/update',
    tags = ['purchase'],
    status_code = status.HTTP_200_OK,
    response_model = purchase_schema.Purchase,
    dependencies=[Depends(get_db)]
)
def purchase_update (
    purchase_id: int = Path(
        ...,
        gt=0
    ),
    current_user: User = Depends(get_current_user)
):
    return purchase_service.update_purchase(purchase_id, current_user)


@router.delete(
    "/{purchase_id}/",
    tags=["purchase"],
    status_code=status.HTTP_200_OK,
    dependencies=[Depends(get_db)]
)
def delete_purchase(
    purchase_id: int = Path(
        ...,
        gt=0
    ),
    current_user: User = Depends(get_current_user)
):
    purchase_service.delete_purchase(purchase_id, current_user)

    return {
        'msg': 'purchase has been deleted sucessfully'
    }
