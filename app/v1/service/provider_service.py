from fastapi import HTTPException, status

from app.v1.schema import provider_schema
from app.v1.model.provider_model import Provider as ProviderModel

def create_provider(provider: provider_schema.ProviderCreate):
    pass

def get_providers():
    pass

def get_provider(provider_id: int):
    pass

def update_provider(provider_id: int, provider: provider_schema.ProviderUpdate):
    pass

def delete_provider(provider_id: int):
    pass
