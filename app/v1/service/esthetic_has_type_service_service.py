from fastapi import HTTPException, status
from app.v1.model import esthetic_has_type_service_model as EstheticHasTypeServiceModel

from app.v1.schema import esthetic_has_type_service_schema
from app.v1.schema import esthetic_schema
from app.v1.schema import type_service_schema


def create_esthetic_has_type_service(
    esthetic_has_type_service: esthetic_has_type_service_schema.EstheticHasTypeServiceCreate
):
    db_esthetic_has_type_service = EstheticHasTypeServiceModel(
        esthetic=esthetic_has_type_service.esthetic,
        type_service=esthetic_has_type_service.type_service
    )

    db_esthetic_has_type_service.save()

    return esthetic_has_type_service_schema.EstheticHasTypeService(
        id=db_esthetic_has_type_service.id,
        esthetic=db_esthetic_has_type_service.esthetic,
        type_service=db_esthetic_has_type_service.type_service
    )


def get_esthetic_has_type_services():
    esthetic_has_type_services = EstheticHasTypeServiceModel.select().order_by(
        EstheticHasTypeServiceModel.id.desc())

    list_esthetic_has_type_services = []
    for esthetic_has_type_service in esthetic_has_type_services:
        list_esthetic_has_type_services.append(
            esthetic_has_type_service_schema.EstheticHasTypeService(
                id=esthetic_has_type_service.id,
                esthetic=esthetic_has_type_service.esthetic,
                type_service=esthetic_has_type_service.type_service
            )
        )

    return esthetic_has_type_service


def get_esthetic_has_type_service(
    esthetic_has_type_service_id: int
):
    esthetic_has_type_service = EstheticHasTypeServiceModel.filter(
        EstheticHasTypeServiceModel.id == esthetic_has_type_service_id).first()

    if not esthetic_has_type_service:
        raise HTTPException(
            status_code=status.HTTP_404_NOT_FOUND,
            detail='Esthetic has type service not found'
        )

    return esthetic_has_type_service_schema.EstheticHasTypeService(
        id=esthetic_has_type_service.id,
        esthetic=esthetic_has_type_service.esthetic,
        type_service=esthetic_has_type_service.type_service
    )


def update_esthetic_has_type_service(
    esthetic_has_type_service_id: int,
    esthetic: int = None,
    type_service: int = None
):
    esthetic_has_type_service = EstheticHasTypeServiceModel.filter(
        EstheticHasTypeServiceModel.id == esthetic_has_type_service_id).first()

    if not esthetic_has_type_service:
        raise HTTPException(
            status_code=status.HTTP_404_NOT_FOUND,
            detail='Esthetic has type service not found'
        )

    esthetic_has_type_service.esthetic = esthetic or esthetic_has_type_service.esthetic
    esthetic_has_type_service.type_service = type_service or esthetic_has_type_service.type_service

    esthetic_has_type_service.save()

    return esthetic_has_type_service_schema.EstheticHasTypeService(
        id=esthetic_has_type_service.id,
        esthetic=esthetic_has_type_service.esthetic,
        type_service=esthetic_has_type_service.type_service
    )


def delete_esthetic_has_type_service(
    esthetic_has_type_service_id: int
):
    esthetic_has_type_service = EstheticHasTypeServiceModel.filter(
        EstheticHasTypeServiceModel.id == esthetic_has_type_service_id).first()

    if not esthetic_has_type_service:
        raise HTTPException(
            status_code=status.HTTP_404_NOT_FOUND,
            detail='Esthetic has type service not found'
        )
    esthetic_has_type_service.delete_instance()
