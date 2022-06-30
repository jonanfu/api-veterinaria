from fastapi import APIRouter, Depends, Body
from fastapi import status
from fastapi import Query
from fastapi import Path

from typing import List, Optional

from app.v1.schema import client_shema
from app.v1.service import client_service
from app.v1.utils.db import get_db
from app.v1.schema.user_schema import User
from app.v1.service.auth_service import get_current_user

router = APIRouter(prefix = '/api/v1/client')

@router.post (
    '/',
    tags = ['client'],
    status_code = status.HTTP_201_CREATED,
    response_model = client_shema.Client,
    dependencies = [Depends(get_db)]
)
def create_client (
    client: client_shema.ClientCreate = Body(...),
    current_user: User = Depends(get_current_user)):
    return client_service.create_client(client, current_user)


@router.get (
    '/',
    tags = ['client'],
    status_code = status.HTTP_200_OK,
    response_model = List[client_shema.Client],
    dependencies = [Depends(get_db)]
)
def get_clients(
    is_done: Optional[bool] = Query(None),
    current_user: User = Depends(get_current_user)
):
    return client_service.get_clients(current_user, is_done)


@router.get (
    '/{client_id}',
    tags = ['client'],
    status_code = status.HTTP_200_OK,
    response_model = client_shema.Client,
    dependencies = [Depends(get_db)]
)
def get_client(
    client_id: int = Path (
        ...,
        gt=0
    ),
    current_user: User = Depends(get_current_user)
):
    return client_service.get_client(client_id, current_user)


@router.put (
    '/{client_id}',
    tags = ['client'],
    status_code = status.HTTP_200_OK,
    response_model = client_shema.Client,
    dependencies = [Depends(get_db)]
)
def update_client(
    client_id: int = Path (
        ...,
        gt=0
    ),
    client: client_shema.ClientUpdate = Body(...),
    current_user: User = Depends(get_current_user)
):
    return client_service.update_client(client_id, client, current_user)


@router.delete (
    '/{client_id}',
    tags = ['client'],
    status_code = status.HTTP_200_OK,
    dependencies = [Depends(get_db)]
)
def delete_client(
    client_id: int = Path (
        ...,
        gt=0
    ),
    current_user: User = Depends(get_current_user)
):
    return client_service.delete_client(client_id, current_user)

