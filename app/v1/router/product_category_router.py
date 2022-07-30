from fastapi import APIRouter, Depends, Body
from fastapi import status
from fastapi import Query
from fastapi import Path

from typing import List, Optional

from app.v1.schema import product_category_schema
from app.v1.service import product_category_service
from app.v1.utils.db import get_db
from app.v1.schema.user_schema import User
from app.v1.service.auth_service import get_current_user

router = APIRouter(prefix = '/api/v1/product_category')


@router.post (
    '/',
    tags = ['product category'],
    status_code = status.HTTP_201_CREATED,
    response_model = product_category_schema.ProductCategory,
    dependencies = [Depends(get_db)]
)
def create_product_category (
    product_category: product_category_schema.ProductCategoryCreate = Body(...)
    ):
    return product_category_service.create_product_category(product_category)


@router.get (
    '/',
    tags = ['product category'],
    status_code = status.HTTP_200_OK,
    response_model = List[product_category_schema.ProductCategory],
    dependencies = [Depends(get_db)]
)
def get_product_category():
    return product_category_service.get_product_categories()


@router.get (
    '/{product_category_id}',
    tags = ['product category'],
    status_code = status.HTTP_200_OK,
    response_model = product_category_schema.ProductCategory,
    dependencies = [Depends(get_db)]
)
def get_product_category(
    product_category_id: int = Path (
        ...,
        gt=0
    )
):
    return product_category_service.get_product_category(product_category_id)


@router.patch (
    '/{product_category_id}/update',
    tags = ['product category'],
    status_code = status.HTTP_200_OK,
    response_model = product_category_schema.ProductCategory,
    dependencies=[Depends(get_db)]
)
def product_category_update (
    product_category_id: int = Path(
        ...,
        gt=0
    ),
    product_category: product_category_schema.ProductCategory = Body(...)
):
    return product_category_service.update_product_category(product_category_id, 
        name = product_category.name,
        photo = product_category.photo,
        description = product_category.description,

    )


@router.delete(
    "/{product_category_id}/",
    tags=["product category"],
    status_code=status.HTTP_200_OK,
    dependencies=[Depends(get_db)]
)
def delete_product_category(
    product_category_id: int = Path(
        ...,
        gt=0
    )
):
    product_category_service.delete_product_category(product_category_id)

    return {
        'msg': 'product category has been deleted sucessfully'
    }
