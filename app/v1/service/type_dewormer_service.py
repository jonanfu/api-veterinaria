from fastapi import HTTPException, status

from app.v1.schema import type_dewormer_schema
from app.v1.model.type_dewormer_model import TypeDewormer as TypeDewormerModel

def create_type_dewormer(type_dewormer: type_dewormer_schema.TypeDewormerCreate):
    db_type_dewormer = TypeDewormerModel(
        name = type_dewormer.name,
        description = type_dewormer.description
    )

    db_type_dewormer.save()

    return type_dewormer_schema.TypeDewormer(
        id = db_type_dewormer.id,
        name = db_type_dewormer.name,
        description = db_type_dewormer.description
    )

def get_type_dewormers():
    type_dewormers = TypeDewormerModel.select().order_by(TypeDewormerModel.id.desc())

    list_type_dewormers = []
    for type_dewormer in type_dewormers:
        list_type_dewormers.append (
            type_dewormer_schema.TypeDewormer(
                id = type_dewormer.id,
                name = type_dewormer.name,
                description = type_dewormer.desciption
            )
        )
    return list_type_dewormers

def get_type_dewormer_by_id(type_dewormer_id: int):
    type_dewormer = TypeDewormerModel.filter(TypeDewormerModel.id == type_dewormer_id).first()

    if not type_dewormer:
        raise HTTPException (
            status_code = status.HTTP_404_NOT_FOUND,
            detail = "Type dewormer not found"
        )

    return type_dewormer_schema.TypeDewormer(
        id = type_dewormer.id,
        name = type_dewormer.name,
        description = type_dewormer.description
    )

def update_type_dewormer(type_dewormer_id: int, 
    name: str = None,
    description: str = None    
    ):

    type_dewormer = TypeDewormerModel.filter(TypeDewormerModel.id == type_dewormer_id).first()

    if not type_dewormer:
        raise HTTPException(
            status_code = status.HTTP_404_NOT_FOUND,
            detail = 'Type dewormer not found'
        )
    
    type_dewormer.name = name or type_dewormer.name
    type_dewormer.description = description or type_dewormer.description

    type_dewormer.save()
    return type_dewormer_schema.TypeDewormer(
        id = type_dewormer.id,
        name = type_dewormer.name,
        description = type_dewormer.description

    )
def delete_type_dewormer(type_dewormer_id: int):
    type_dewormer = TypeDewormerModel.filter(TypeDewormerModel.id == type_dewormer_id).first()

    if not type_dewormer:
        raise HTTPException(
            status_code = status.HTTP_404_NOT_FOUND,
            detail = 'Type dewormer not found'
        )

    type_dewormer.delete_instance()
