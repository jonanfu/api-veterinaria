from fastapi import APIRouter, Depends, Body
from fastapi import status
from fastapi import Query
from fastapi import Path

from typing import List, Optional

from app.v1.schema import product_schema
from app.v1.service import product_service
from app.v1.utils.db import get_db
from app.v1.schema.user_schema import User
from app.v1.service.auth_service import get_current_user

router = APIRouter(prefix='/api/v1/product')


@router.post(
    '/',
    tags=['product'],
    status_code=status.HTTP_201_CREATED,
    response_model=product_schema.Product,
    dependencies=[Depends(get_db)]
)
def create_product(
    product: product_schema.ProductCreate = Body(...),
):
    return product_service.create_product(product)


@router.get(
    '/',
    tags=['product'],
    status_code=status.HTTP_200_OK,
    response_model=List[product_schema.Product],
    dependencies=[Depends(get_db)]
)
def get_product():
    return product_service.get_products()


@router.get(
    '/{product_id}',
    tags=['product'],
    status_code=status.HTTP_200_OK,
    response_model=product_schema.Product,
    dependencies=[Depends(get_db)]
)
def get_product(
    product_id: int = Path(
        ...,
        gt=0
    )
):
    return product_service.get_task(product_id)


@router.patch(
    '/{product_id}/update',
    tags=['product'],
    status_code=status.HTTP_200_OK,
    response_model=product_schema.Product,
    dependencies=[Depends(get_db)]
)
def product_update(
    product_id: int = Path(
        ...,
        gt=0
    ),
    product: product_schema.Product = Body(...)
):
    return product_service.update_product(product_id,
                                          name=product.name,
                                          internal_code=product.internal_code,
                                          barcode=product.barcode,
                                          price=product.price,
                                          stock=product.stock,
                                          minimun_amount=product.minimun_amount,
                                          due_date=product.due_date,
                                          location=product.location,
                                          product_category=product.product_category,
                                          provider=product.provider

                                          )


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
    )
):
    product_service.delete_product(product_id)

    return {
        'msg': 'product has been deleted sucessfully'
    }
