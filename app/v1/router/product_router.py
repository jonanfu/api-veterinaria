from fastapi import APIRouter, Depends, Body
from fastapi import status
from fastapi import Query
from fastapi import Path

from typing import List, Optional

from app.v1.schema import product_schema
from app.v1.schema import product_category_schema
from app.v1.schema import provider_schema
from app.v1.service import product_service
from app.v1.utils import get_db
from app.v1.schema.user_schema import User
from app.v1.service.auth_service import get_current_user

router = APIRouter(prefix = '/api/v1/product')


@router.post (
    '/',
    tags = ['product'],
    status_code = status.HTTP_201_CREATED,
    response_model = product_schema.Product,
    dependencies = [Depends(get_db)]
)
def create_product (
    product: product_schema.ProductCreate = Body(...),
    current_user: User = Depends(get_current_user)):
    return product_service.create_product(product, current_user)


@router.get (
    '/',
    tags = ['product'],
    status_code = status.HTTP_200_OK,
    response_model = List[product_schema.Product],
    dependencies = [Depends(get_db)]
)
def get_product(
    is_done: Optional[bool] = Query(None),
    current_user: User = Depends(get_current_user)
):
    return product_service.get_products(current_user, is_done)


@router.get (
    '/{product_id}',
    tags = ['product'],
    status_code = status.HTTP_200_OK,
    response_model = product_schema.Product,
    dependencies = [Depends(get_db)]
)
def get_product(
    product_id: int = Path (
        ...,
        gt=0
    ),
    current_user: User = Depends(get_current_user)
):
    return product_service.get_task(product_id, current_user)


@router.patch (
    '/{product_id}/update',
    tags = ['product'],
    status_code = status.HTTP_200_OK,
    response_model = product_schema.Product,
    dependencies=[Depends(get_db)]
)
def product_update (
    product_id: int = Path(
        ...,
        gt=0
    ),
    current_user: User = Depends(get_current_user)
):
    return product_service.update_product(product_id, current_user)


@router.delete(
    "/{product_id}/",
    tags=["product"],
    status_code=status.HTTP_200_OK,
    dependencies=[Depends(get_db)]
)
def delete_product(
    product_id: int = Path(
        ...,
        gt=0
    ),
    current_user: User = Depends(get_current_user)
):
    product_service.delete_product(product_id, current_user)

    return {
        'msg': 'product has been deleted sucessfully'
    }
