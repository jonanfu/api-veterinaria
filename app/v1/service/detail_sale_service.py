from fastapi import HTTPException, status

from app.v1.schema import detail_sale_schema
from app.v1.model import detail_sale_model as DetailSaleModel


def create_detail_sale(
    detail_sale: detail_sale_schema.DetailSaleCreate,
):
    db_detail_sale = DetailSaleModel(
        amount=detail_sale.amount,
        price=detail_sale.price,
        tax=detail_sale.tax,
        subtotal=detail_sale.subtotal,
        discount=detail_sale.discount,

        sale=detail_sale.sale,
        product=detail_sale.product

    )

    db_detail_sale.save()

    return detail_sale.DetailSale(
        id=db_detail_sale.id,
        amount=db_detail_sale.amount,
        price=db_detail_sale.price,
        tax=db_detail_sale.tax,
        subtotal=db_detail_sale.subtotal,
        discount=db_detail_sale.discount,

        sale=db_detail_sale.sale,
        product=db_detail_sale.product
    )


def get_detail_sales():
    detail_sales = DetailSaleModel.Select().order_by(DetailSaleModel.id.desc())

    list_detail_sales = []
    for detail_sale in detail_sales:
        list_detail_sales.append(
            detail_sale_schema.DetailSale(
                id=detail_sale.id,
                amount=detail_sale.amount,
                price=detail_sale.price,
                tax=detail_sale.tax,
                subtotal=detail_sale.subtotal,
                discount=detail_sale.discount,

                sale=detail_sale.sale,
                product=detail_sale.product
            )
        )


def get_detail_sale(
    detail_sale_id: int,
):
    detail_sale = DetailSaleModel.filter(
        DetailSaleModel.id == detail_sale_id).first()

    if not detail_sale_id:
        raise HTTPException(
            status_code=status.HTTP_404_NOT_FOUND,
            detail='Detail sale not found'
        )

    return detail_sale_schema.DetailSale(
        id=detail_sale.id,
        amount=detail_sale.amount,
        price=detail_sale.price,
        tax=detail_sale.tax,
        subtotal=detail_sale.subtotal,
        discount=detail_sale.discount,

        sale=detail_sale.sale,
        product=detail_sale.product
    )


def update_detail_sale(
    detail_sale_id: int,
        amount: int = None,
    price: float = None,
    tax: float = None,
    subtotal: float = None,
    discount: float = None,

    sale: int = None,
    product: int = None
):
    detail_sale = DetailSaleModel.filter(
        DetailSaleModel.id == detail_sale_id).first()

    if not detail_sale:
        raise HTTPException(
            status_code=status.HTTP_404_NOT_FOUND,
            detail='Detail sale not found'
        )
    detail_sale.amount = amount or detail_sale.amount
    detail_sale.price = price or detail_sale.price
    detail_sale.tax = tax or detail_sale.tax
    detail_sale.subtotal = subtotal or detail_sale.subtotal
    detail_sale.discount = discount or detail_sale.discount

    detail_sale.sale = sale or detail_sale.sale
    detail_sale.product = product or detail_sale.product

    detail_sale.save()

    return detail_sale_schema.DetailSale(
        id=detail_sale.id,
        amount=detail_sale.amount,
        price=detail_sale.price,
        tax=detail_sale.tax,
        subtotal=detail_sale.subtotal,
        discount=detail_sale.discount,

        sale=detail_sale.sale,
        product=detail_sale.product
    )


def delete_detail_sale(detail_sale_id: int):
    detail_sale = DetailSaleModel.filter(
        DetailSaleModel.id == detail_sale_id).first()

    if not detail_sale:
        raise HTTPException(
            status_code=status.HTTP_404_NOT_FOUND,
            detail='Detail sale not found'
        )

    detail_sale.delete_instance()
