from fastapi import HTTPException, status

from app.v1.schema import product_category_schema
from app.v1.model.product_category_model import ProductCategory as ProductCategoryModel

def create_product_category(product_category: product_category_schema.ProductCategoryCreate):
    db_product_category = ProductCategoryModel(
        name = product_category.name,
        photo = product_category.photo,
        description = product_category.description
    )

    db_product_category.save()

    return product_category_schema.ProductCategory(
        id = db_product_category.id,
        name = db_product_category.name,
        photo = db_product_category.photo,
        description = db_product_category.description
    )

def get_product_categories():
    product_categories = ProductCategoryModel.select().order_by(ProductCategoryModel.id.desc())

    list_product_categories = []
    for product_category in product_categories:
        list_product_categories.append(
            product_category_schema.ProductCategory(
                id = product_category.id,
                name = product_category.name,
                photo = product_category.photo,
                description = product_category.description
            )
        )
    
    return list_product_categories

def get_product_category(product_category_id: int):
    product_category = ProductCategoryModel.filter(ProductCategoryModel.id == product_category_id).first()

    if not product_category:
        raise HTTPException(
            status_code = status.HTTP_404_NOT_FOUND,
            detail = "Product category not found"
        )

    return product_category_schema.ProductCategory(
        id = product_category.id,
        name = product_category.name,
        photo = product_category.photo,
        description = product_category.description
    )


def update_product_category(product_category_id: int,
    name = None,
    photo = None,
    description = None):
    
    product_category = ProductCategoryModel.filter(ProductCategoryModel.id == product_category_id).first()

    if not product_category:
        raise HTTPException(
            status_code = status.HTTP_404_NOT_FOUND,
            detail = "Product category not found"
        )

    product_category.name = name
    product_category.photo = photo
    product_category.description = description
    product_category.save()

    return product_category_schema.ProductCategory(
        id = product_category.id,
        name = product_category.name,
        photo = product_category.photo,
        description = product_category.description
    )
    
    

def delete_product_category(product_category_id: int):
    product_category = ProductCategoryModel.filter(ProductCategoryModel.id == product_category_id).first()

    if not product_category:
        raise HTTPException(
            status_code = status.HTTP_404_NOT_FOUND,
            detail = "Product category not found"
        )
    
    product_category.delete_instance()
    
