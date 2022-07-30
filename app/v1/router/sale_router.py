from fastapi import APIRouter, Depends, Body
from fastapi import status
from fastapi import Query
from fastapi import Path

from typing import List, Optional

from app.v1.schema import sale_schema
from app.v1.service import sale_service
from app.v1.utils.db import get_db
from app.v1.schema.user_schema import User
from app.v1.service.auth_service import get_current_user

router = APIRouter(prefix='/api/v1/sale')


@router.post(
    '/',
    tags=['sale'],
    status_code=status.HTTP_201_CREATED,
    response_model=sale_schema.Sale,
    dependencies=[Depends(get_db)]
)
def create_sale(
        sale: sale_schema.SaleCreate = Body(...),
        current_user: User = Depends(get_current_user)):
    return sale_service.create_sale(sale, current_user)


@router.get(
    '/',
    tags=['sale'],
    status_code=status.HTTP_200_OK,
    response_model=List[sale_schema.Sale],
    dependencies=[Depends(get_db)]
)
def get_sale():
    return sale_service.get_sales()


@router.get(
    '/{sale_id}',
    tags=['sale'],
    status_code=status.HTTP_200_OK,
    response_model=sale_schema.Sale,
    dependencies=[Depends(get_db)]
)
def get_sale(
    sale_id: int = Path(
        ...,
        gt=0
    )
):
    return sale_service.get_sale(sale_id)


@router.patch(
    '/{sale_id}/update',
    tags=['sale'],
    status_code=status.HTTP_200_OK,
    response_model=sale_schema.Sale,
    dependencies=[Depends(get_db)]
)
def sale_update(
    sale_id: int = Path(
        ...,
        gt=0
    ),
    sale: sale_schema.Sale = Body(...)
):
    return sale_service.update_sale(sale_id,
                                    status=sale.status
                                    )


@router.delete(
    "/{sale_id}/",
    tags=["sale"],
    status_code=status.HTTP_200_OK,
    dependencies=[Depends(get_db)]
)
def delete_sale(
    sale_id: int = Path(
        ...,
        gt=0
    )
):
    sale_service.delete_sale(sale_id)

    return {
        'msg': 'sale has been deleted sucessfully'
    }
