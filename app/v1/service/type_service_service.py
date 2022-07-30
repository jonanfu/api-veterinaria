from fastapi import HTTPException, status

from app.v1.schema import type_service_schema
from app.v1.model.type_service_model import TypeService as TypeServiceModel

def create_type_service(type_service: type_service_schema.TypeServiceCreate):
    db_type_service = TypeServiceModel(
        name = type_service.name,
        description = type_service.description
    )

    db_type_service.save()

    return type_service_schema.TypeService(
        id = db_type_service.id,
        name = db_type_service.name,
        description = db_type_service.description
    )

def get_type_services():
    type_services = TypeServiceModel.select().order_by(TypeServiceModel.id.desc())

    list_type_services = []
    for type_service in type_services:
        list_type_services.append (
            type_service_schema.TypeService(
                id = type_service.id,
                name = type_service.name,
                description = type_service.desciption
            )
        )
    return list_type_services

def get_type_service_by_id(type_service_id: int):
    type_service = TypeServiceModel.filter(TypeServiceModel.id == type_service_id).first()

    if not type_service:
        raise HTTPException (
            status_code = status.HTTP_404_NOT_FOUND,
            detail = "Type service not found"
        )

    return type_service_schema.TypeService(
        id = type_service.id,
        name = type_service.name,
        description = type_service.description
    )

def update_type_service(type_service_id: int, 
    name: str = None,
    description: str = None    
    ):

    type_service = TypeServiceModel.filter(TypeServiceModel.id == type_service_id).first()

    if not type_service:
        raise HTTPException(
            status_code = status.HTTP_404_NOT_FOUND,
            detail = 'Type service not found'
        )
    
    type_service.name = name or type_service.name
    type_service.description = description or type_service.description

    type_service.save()
    return type_service_schema.TypeService(
        id = type_service.id,
        name = type_service.name,
        description = type_service.description

    )
def delete_type_service(type_service_id: int):
    type_service = TypeServiceModel.filter(TypeServiceModel.id == type_service_id).first()

    if not type_service:
        raise HTTPException(
            status_code = status.HTTP_404_NOT_FOUND,
            detail = 'Type service not found'
        )

    type_service.delete_instance()
