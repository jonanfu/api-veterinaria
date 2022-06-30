from fastapi import APIRouter, Depends, Body
from fastapi import status
from fastapi import Query
from fastapi import Path

from typing import List, Optional

from app.v1.schema import provider_schema
from app.v1.service import provider_service
from app.v1.utils import get_db
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
    current_user: User = Depends(get_current_user)):
    return provider_service.create_provider(provider, current_user)


@router.get (
    '/',
    tags = ['provider'],
    status_code = status.HTTP_200_OK,
    response_model = List[provider_schema.Provider],
    dependencies = [Depends(get_db)]
)
def get_provider(
    is_done: Optional[bool] = Query(None),
    current_user: User = Depends(get_current_user)
):
    return provider_service.get_providers(current_user, is_done)


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
    ),
    current_user: User = Depends(get_current_user)
):
    return provider_service.get_task(provider_id, current_user)


@router.patch (
    '/{provider_id}/update',
    tags = ['provider'],
    status_code = status.HTTP_200_OK,
    response_model = provider_schema.Provider,
    dependencies=[Depends(get_db)]
)
def provider_update (
    provider_id: int = Path(
        ...,
        gt=0
    ),
    current_user: User = Depends(get_current_user)
):
    return provider_service.update_provider(provider_id, current_user)


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
    ),
    current_user: User = Depends(get_current_user)
):
    provider_service.delete_provider(provider_id, current_user)

    return {
        'msg': 'provider has been deleted sucessfully'
    }
