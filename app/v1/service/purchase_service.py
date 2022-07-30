from fastapi import HTTPException, status

from app.v1.schema import purchase_schema
from app.v1.model.purchase_model import Purchase as PurchaseModel


def create_purchase(purchase: purchase_schema.PurchaseCreate):
    db_purchase = PurchaseModel(
        total=purchase.total,
        image=purchase.image
    )

    return purchase_schema.Purchase(
        id=db_purchase.id,
        date=db_purchase.date,
        total=db_purchase.total,
        status=db_purchase.status,
        image=db_purchase.image
    )


def get_purchases():
    purchases = PurchaseModel.select().order_by(PurchaseModel.id.desc())

    list_purchases = []
    for purchase in purchases:
        list_purchases.append(
            purchase_schema.Purchase(
                id=purchase.id,
                date=purchase.date,
                total=purchase.total,
                status=purchase.status,
                image=purchase.image
            )
        )

    return list_purchases


def get_purchase(purchase_id: int):
    purchase = PurchaseModel.filter(PurchaseModel.id == purchase_id).first()

    if not purchase:
        raise HTTPException(
            status_code=status.HTTP_404_NOT_FOUND,
            detail='Purchase not found'
        )

    return purchase_schema.Purchase(
        id=purchase.id,
        date=purchase.date,
        total=purchase.total,
        status=purchase.status,
        image=purchase.image
    )


def update_purchase(purchase_id: int,
                    status: float = None,
                    image: str = None
                    ):
    purchase = PurchaseModel.filter(PurchaseModel.id == purchase_id).first()

    if not purchase:
        raise HTTPException(
            status_code=status.HTTP_404_NOT_FOUND,
            detail='Purchase not found'
        )

    purchase.total = status or purchase.status
    purchase.image = image or purchase.image

    purchase.save()

    return purchase_schema.Purchase(
        id=purchase.id,
        date=purchase.date,
        total=purchase.total,
        status=purchase.status,
        image=purchase.image
    )


def delete_purchase(purchase_id: int):
    purchase = PurchaseModel.filter(PurchaseModel.id == purchase_id).first()

    if not purchase:
        raise HTTPException(
            status_code=status.HTTP_404_NOT_FOUND,
            detail='Purchase not found'
        )

    purchase.delete_instance()
