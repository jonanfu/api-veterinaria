from datetime import datetime
from fastapi import HTTPException, status
from app.v1.model.provider_model import Provider

from app.v1.schema import product_schema
from app.v1.model import product_model as ProductModel


def create_product(
    product: product_schema.ProductCreate,

):
    db_product = ProductModel(
        name=product.name,
        internal_code=product.internal_code,
        barcode=product.barcode,
        price=product.price,
        stock=product.stock,
        minimun_amount=product.minimun_amount,
        due_date=product.due_data,
        location=product.location,

        product_category=product.product_category,
        provider=product.provider
    )

    return product_schema.Product(
        id=db_product.id,
        name=db_product.name,
        internal_code=db_product.internal_code,
        barcode=db_product.barcode,
        price=db_product.price,
        stock=db_product.stock,
        minimun_amount=db_product.minimun_amount,
        due_date=db_product.due_data,
        location=db_product.location,

        product_category=db_product.product_category,
        provider=db_product.provider
    )


def get_products():
    products = ProductModel.Select().order_by(ProductModel.id.desc())

    list_products = []
    for product in products:
        list_products.append(
            product_schema.Product(
                id=product.id,
                name=product.name,
                internal_code=product.internal_code,
                barcode=product.barcode,
                price=product.price,
                stock=product.stock,
                minimun_amount=product.minimun_amount,
                due_date=product.due_data,
                location=product.location,

                product_category=product.product_category,
                provider=product.provider
            )
        )


def get_product(product_id: int):
    product = ProductModel.filter(ProductModel.id == product_id).first()

    if not product:
        raise HTTPException(
            status_code=status.HTTP_404_NOT_FOUND,
            detail='Product not found'
        )

    return product_schema.Product(
        id=product.id,
        name=product.name,
        internal_code=product.internal_code,
        barcode=product.barcode,
        price=product.price,
        stock=product.stock,
        minimun_amount=product.minimun_amount,
        due_date=product.due_data,
        location=product.location,

        product_category=product.product_category,
        provider=product.provider
    )


def update_product(product_id: int,
                   name: str = None,
                   internal_code: str = None,
                   barcode: str = None,
                   price: float = None,
                   stock: int = None,
                   minimun_amount: int = None,
                   due_date: datetime = None,
                   location: str = None,
                   product_category: int = None,
                   provider: int = Provider
                   ):
    product = ProductModel.filter(ProductModel.id == product_id).first()

    if not product:
        raise HTTPException(
            status_code=status.HTTP_404_NOT_FOUND,
            detail='Product not found'
        )

    product.name = name or product.name


    product.internal_code = internal_code or product.internal_code
    product.barcode = barcode or product.barcode
    product.price = price or product.price
    product.stock = stock or product.stock
    product.minimun_amount = minimun_amount or product.minimun_amount
    product.due_date = due_date or product.due_date
    product.location = location or product.location

    product.product_category = product_category or product.product_category
    product.provider = provider or product.provider

    return product_schema.Product(
        id=product.id,
        name=product.name,
        internal_code=product.internal_code,
        barcode=product.barcode,
        price=product.price,
        stock=product.stock,
        minimun_amount=product.minimun_amount,
        due_date=product.due_data,
        location=product.location,

        product_category=product.product_category,
        provider=product.provider
    )


def delete_product(product_id: int):
    product = ProductModel.filter(ProductModel.id == product_id).first()

    if not product:
        raise HTTPException(
            status_code=status.HTTP_404_NOT_FOUND,
            detail='Product not found'
        )

    product.delete_instance()
