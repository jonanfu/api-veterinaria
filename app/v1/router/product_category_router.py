from fastapi import APIRouter, Depends, Body
from fastapi import status
from fastapi import Query
from fastapi import Path

from typing import List, Optional

from app.v1.schema import product_category_schema
from app.v1.service import product_category_service
from app.v1.utils import get_db
from app.v1.schema.user_schema import User
from app.v1.service.auth_service import get_current_user

router = APIRouter(prefix = '/api/v1/product_category')


@router.post (
    '/',
    tags = ['product_category'],
    status_code = status.HTTP_201_CREATED,
    response_model = product_category_schema.ProductCategory,
    dependencies = [Depends(get_db)]
)
def create_product_category (
    product_category: product_category_schema.ProductCategoryCreate = Body(...),
    current_user: User = Depends(get_current_user)):
    return product_category_service.create_product_category(product_category, current_user)


@router.get (
    '/',
    tags = ['product_category'],
    status_code = status.HTTP_200_OK,
    response_model = List[product_category_schema.ProductCategory],
    dependencies = [Depends(get_db)]
)
def get_product_category(
    is_done: Optional[bool] = Query(None),
    current_user: User = Depends(get_current_user)
):
    return product_category_service.get_product_categorys(current_user, is_done)


@router.get (
    '/{product_category_id}',
    tags = ['product-category'],
    status_code = status.HTTP_200_OK,
    response_model = product_category_schema.ProductCategory,
    dependencies = [Depends(get_db)]
)
def get_product_category(
    product_category_id: int = Path (
        ...,
        gt=0
    ),
    current_user: User = Depends(get_current_user)
):
    return product_category_service.get_product_category(product_category_id, current_user)


@router.patch (
    '/{product_category_id}/update',
    tags = ['product-category'],
    status_code = status.HTTP_200_OK,
    response_model = product_category_schema.ProductCategory,
    dependencies=[Depends(get_db)]
)
def product_category_update (
    product_category_id: int = Path(
        ...,
        gt=0
    ),
    current_user: User = Depends(get_current_user)
):
    return product_category_service.update_product_category(product_category_id, current_user)


@router.delete(
    "/{product_category_id}/",
    tags=["product-category"],
    status_code=status.HTTP_200_OK,
    dependencies=[Depends(get_db)]
)
def delete_product_category(
    product_category_id: int = Path(
        ...,
        gt=0
    ),
    current_user: User = Depends(get_current_user)
):
    product_category_service.delete_product_category(product_category_id, current_user)

    return {
        'msg': 'product category has been deleted sucessfully'
    }
