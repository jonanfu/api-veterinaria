from fastapi import HTTPException, status

from app.v1.schema import esthetic_has_type_service_schema
from app.v1.schema import esthetic_schema
from app.v1.schema import type_service_schema

def create_esthetic_has_type_service(
    esthetic_has_type_service: esthetic_has_type_service_schema.EstheticHasTypeServiceCreate,
    esthetic: esthetic_schema.Esthetic,
    type_service: type_service_schema.TypeService
    ):
    pass

def get_esthetic_has_type_services():
    pass

def get_esthetic_has_type_service(
    esthetic_has_type_service_id: int
    ):
    pass

def update_esthetic_has_type_service(
    esthetic_has_type_service_id: int,
    esthetic_has_type_service: esthetic_has_type_service_schema.EstheticHasTypeServiceUpdate
    ):
    pass

def delete_esthetic_has_type_service(
    esthetic_has_type_service_id: int
    ):
    pass
