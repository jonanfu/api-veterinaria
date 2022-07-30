from fastapi import HTTPException, status

from app.v1.schema import provider_schema
from app.v1.model.provider_model import Provider as ProviderModel

def create_provider(provider: provider_schema.ProviderCreate):
    db_provider = ProviderModel(
        name = provider.name,
        phone = provider.phone,
        ruc = provider.ruc,
        email = provider.email,
        country = provider.country,
        province = provider.province,
        city = provider.city,
        address = provider.address,
        postal_code = provider.postal_code
    )

    db_provider.save()

    return provider_schema.Provider (
        id = db_provider.id,
        name = db_provider.name,
        ruc = db_provider.ruc,
        email = db_provider.email,
        country = db_provider.country,
        province = db_provider.province,
        city = db_provider.city,
        address = db_provider.address,
        postal_code = db_provider.postal_code,
    )

def get_providers():
    providers = ProviderModel.select().order_by(ProviderModel.id.desc())

    list_providers = []
    for provider in providers:
        list_providers.append(
            provider_schema.Provider(
                id = provider.id,
                name = provider.name,
                ruc = provider.ruc,
                email = provider.email,
                country = provider.country,
                province = provider.province,
                city = provider.city,
                address = provider.address,
                posta_code = provider.postal_code
            )
        )

def get_provider(provider_id: int):
    provider = ProviderModel.filter(ProviderModel.id == provider_id).first()

    if not provider:
        raise HTTPException (
            status_code = status.HTTP_404_NOT_FOUND,
            detail = "Provider not found"
        )

    return provider_schema.Provider(
        id = provider.id,
        name = provider.name,
        ruc = provider.ruc,
        email = provider.email,
        country = provider.country,
        province = provider.province,
        city = provider.city,
        address = provider.address,
        postal_code = provider.postal_code
    )

def update_provider(provider_id: int,
    name: str = None,
    ruc: str = None,
    email: str = None,
    country: str = None,
    province: str = None,
    city: str = None,
    address: str = None,
    postal_code: str = None,
    ):

    provider = ProviderModel.filter(ProviderModel.id == provider_id).first()

    if not provider:
        raise HTTPException (
            status_code = status.HTTP_404_NOT_FOUND,
            detail = 'Provider not found'
        )
    
    provider.name = name or provider.name
    provider.ruc = ruc or provider.ruc
    provider.email = email or provider.email
    provider.country = country or provider.country
    provider.province = province or provider.province
    provider.city = city or provider.city
    provider.address = address or provider.address
    provider.postal_code = postal_code or provider.postal_code

    provider.save()

    return provider_schema.Provider(
        id = provider.id,
        name = provider.name,
        ruc = provider.ruc,
        email = provider.email,
        country = provider.country,
        province = provider.province,
        city = provider.city,
        address = provider.address,
        postal_code = provider.postal_code,
    )

    

def delete_provider(provider_id: int):
    provider = ProviderModel.filter(ProviderModel.id == provider_id).first()

    if not provider:
        raise HTTPException (
            status_code = status.HTTP_404_NOT_FOUND
        )

    provider.delete_instance()