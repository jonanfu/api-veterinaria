from fastapi import HTTPException, status

from app.v1.schema import type_service_schema
from app.v1.model import type_service_model as TypeServiceModel

def create_type_service(type_service: type_service_schema.TypeServiceCreate):
    pass

def get_type_services():
    pass

def get_type_service(type_service_id: int):
    pass

def update_type_service(type_service_id: int, type_service: type_service_schema.TypeServiceUpdate):
    pass

def delete_type_service(type_service_id: int):
    pass
