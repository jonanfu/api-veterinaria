from fastapi import APIRouter, Depends, Body
from fastapi import status
from fastapi import Query
from fastapi import Path

from typing import List, Optional

from app.v1.schema import provider_schema
from app.v1.service import provider_service
from app.v1.utils.db import get_db
from app.v1.schema.user_schema import User
from app.v1.service.auth_service import get_current_user

router = APIRouter(prefix = '/api/v1/provider')


@router.post (
    '/',
    tags = ['provider'],
    status_code = status.HTTP_201_CREATED,
    response_model = provider_schema.Provider,
    dependencies = [Depends(get_db)]
)
def create_provider (
    provider: provider_schema.ProviderCreate = Body(...),
    ):
    return provider_service.create_provider(provider)


@router.get (
    '/',
    tags = ['provider'],
    status_code = status.HTTP_200_OK,
    response_model = List[provider_schema.Provider],
    dependencies = [Depends(get_db)]
)
def get_provider():
    return provider_service.get_providers()


@router.get (
    '/{provider_id}',
    tags = ['provider'],
    status_code = status.HTTP_200_OK,
    response_model = provider_schema.Provider,
    dependencies = [Depends(get_db)]
)
def get_provider(
    provider_id: int = Path (
        ...,
        gt=0
    )
):
    return provider_service.get_provider(provider_id)


@router.patch (
    '/{provider_id}/update',
    tags = ['provider'],
    status_code = status.HTTP_200_OK,
    response_model = provider_schema.Provider,
    dependencies=[Depends(get_db)]
)
def update_provider (
    provider_id: int = Path(
        ...,
        gt=0
    ),
    provider: provider_schema.Provider = Body(...)
):
    return provider_service.update_provider(provider_id,
        name = provider.name,
        ruc = provider.ruc,
        email = provider.email,
        country = provider.country,
        province = provider.province,
        city = provider.city,
        address = provider.address,
        posta_code = provider.postal_code,
        )


@router.delete(
    "/{provider_id}/",
    tags=["provider"],
    status_code=status.HTTP_200_OK,
    dependencies=[Depends(get_db)]
)
def delete_provider(
    provider_id: int = Path(
        ...,
        gt=0
    )
):

    return provider_service.delete_provider(provider_id)
