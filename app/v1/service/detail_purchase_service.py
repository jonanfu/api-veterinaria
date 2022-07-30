from fastapi import HTTPException, status

from app.v1.schema import detail_purchase_schema
from app.v1.model import detail_purchase_model as DetailPurchaseModel


def create_detail_purchase(
    detail_purchase: detail_purchase_schema.DetailPurchaseCreate,
):
    db_detail_purchase = DetailPurchaseModel(
        amount=detail_purchase.amount,
        price=detail_purchase.price,
        tax=detail_purchase.tax,
        subtotal=detail_purchase.subtotal,
        profit_percentage=detail_purchase.profit_percentage,

        purchase=detail_purchase.purchase,
        product=detail_purchase.product

    )

    db_detail_purchase.save()

    return detail_purchase_schema.DetailPurchase(
        id=db_detail_purchase.id,
        amount=db_detail_purchase.amount,
        price=db_detail_purchase.price,
        tax=db_detail_purchase.tax,
        subtotal=db_detail_purchase.subtotal,
        profit_percentage=db_detail_purchase.profit_percentage,

        purchase=db_detail_purchase.purchase,
        product=db_detail_purchase.product
    )


def get_detail_purchases():
    detail_purchases = DetailPurchaseModel.Select().order_by(
        DetailPurchaseModel.id.desc())

    list_detail_purchases = []
    for detail_purchase in detail_purchases:
        list_detail_purchases.append(
            detail_purchase_schema.DetailPurchase(
                id=detail_purchase.id,
                amount=detail_purchase.amount,
                price=detail_purchase.price,
                tax=detail_purchase.tax,
                subtotal=detail_purchase.subtotal,
                profit_percentage=detail_purchase.profit_percentage,

                purchase=detail_purchase.purchase,
                product=detail_purchase.product
            )
        )
    return list_detail_purchases


def get_detail_purchase(
    detail_purchase_id: int,
):
    detail_purchase = DetailPurchaseModel.filter(
        DetailPurchaseModel.id == detail_purchase_id).first()

    if not detail_purchase:
        raise HTTPException(
            status_code=status.HTTP_404_NOT_FOUND,
            detail='Detail purchase not found'
        )

    return detail_purchase_schema.DetailPurchase(
        id=detail_purchase.id,
        amount=detail_purchase.amount,
        price=detail_purchase.price,
        tax=detail_purchase.tax,
        subtotal=detail_purchase.subtotal,
        profit_percentage=detail_purchase.profit_percentage,

        purchase=detail_purchase.purchase,
        product=detail_purchase.product
    )


def update_detail_purchase(
    detail_purchase_id: int,
    amount: int = None,
    price: float = None,
    tax: float = None,
    subtotal: float = None,
    profit_percentage: float = None,

    purchase: int = None,
    product: int = None
):
    detail_purchase = DetailPurchaseModel.filter(
        DetailPurchaseModel.id == detail_purchase_id).first()

    if not detail_purchase:
        raise HTTPException(
            status_code=status.HTTP_404_NOT_FOUND,
            detail='Detail purchase not found'
        )
    detail_purchase.amount = amount or detail_purchase.amount
    detail_purchase.price = price or detail_purchase.price
    detail_purchase.tax = tax or detail_purchase.tax
    detail_purchase.subtotal = subtotal or detail_purchase.subtotal
    detail_purchase.profit_percentage = profit_percentage or detail_purchase.profit_percentage

    detail_purchase.purchase = purchase or detail_purchase.purchase
    detail_purchase.product = product or detail_purchase.product

    return detail_purchase_schema.DetailPurchase(
        id=detail_purchase.id,
        amount=detail_purchase.amount,
        price=detail_purchase.price,
        tax=detail_purchase.tax,
        subtotal=detail_purchase.subtotal,
        profit_percentage=detail_purchase.profit_percentage,

        purchase=detail_purchase.purchase,
        product=detail_purchase.product
    )


def delete_detail_purchase(detail_purchase_id: int):
    detail_purchase = DetailPurchaseModel.filter(
        DetailPurchaseModel.id == detail_purchase_id).first()

    if not detail_purchase:
        raise HTTPException(
            status_code=status.HTTP_404_NOT_FOUND,
            detail='Detail purchase not found'
        )

    detail_purchase.delete_instance()
