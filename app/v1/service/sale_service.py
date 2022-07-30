from fastapi import HTTPException, status

from app.v1.schema import sale_schema
from app.v1.model.sale_model import Sale as SaleModel


def create_sale(sale: sale_schema.SaleCreate):
    db_sale = SaleModel(
        total=sale.total
    )

    db_sale.save()

    return sale_schema.Sale(
        id=db_sale.id,
        date=db_sale.date,
        total=db_sale.total,
        status=db_sale.status
    )


def get_sales():
    sales = SaleModel.select().order_by(SaleModel.id.desc())

    list_sales = []
    for sale in sales:
        list_sales.append(
            sale_schema.Sale(
                id=sale.id,
                date=sale.date,
                total=sale.total,
                status=sale.status
            )
        )

    return list_sales


def get_sale(sale_id: int):
    sale = SaleModel.filter(SaleModel.id == sale_id).first()

    if not sale:
        raise HTTPException(
            status_code=status.HTTP_404_NOT_FOUND,
            detail='Sale not found'
        )

    return sale_schema.Sale(
        id=sale.id,
        date=sale.date,
        total=sale.total,
        status=sale.status
    )


def update_sale(sale_id: int,
                status: bool = None
                ):
    sale = SaleModel.filter(SaleModel.id == sale_id).first()

    if not sale:
        raise HTTPException(
            status_code=status.HTTP_404_NOT_FOUND,
            detail='Sale not found'
        )

    sale.status = status or sale.status

    sale.save()

    return sale_schema.Sale(
        id=sale.id,
        date=sale.date,
        total=sale.total,
        status=sale.status
    )


def delete_sale(sale_id: int):
    sale = SaleModel.filter(SaleModel.id == sale_id).first()

    if not sale:
        raise HTTPException(
            status_code=status.HTTP_404_NOT_FOUND,
            detail='Sale not found'
        )

    sale.delete_instance()
