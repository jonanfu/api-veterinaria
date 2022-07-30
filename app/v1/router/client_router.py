from fastapi import APIRouter, Depends, Body
from fastapi import status
from fastapi import Query
from fastapi import Path

from typing import List, Optional

from app.v1.schema import client_schema
from app.v1.service import client_service
from app.v1.utils.db import get_db
from app.v1.schema.user_schema import User
from app.v1.service.auth_service import get_current_user

router = APIRouter(prefix = '/api/v1/client')

@router.post (
    '/',
    tags = ['client'],
    status_code = status.HTTP_201_CREATED,
    response_model = client_schema.Client,
    dependencies = [Depends(get_db)]
)
def create_client (
    client: client_schema.ClientCreate = Body(...),
    ):
    return client_service.create_client(client)


@router.get (
    '/',
    tags = ['client'],
    status_code = status.HTTP_200_OK,
    response_model = List[client_schema.Client],
    dependencies = [Depends(get_db)]
)
def get_clients():
    return client_service.get_clients()


@router.get (
    '/{client_id}',
    tags = ['client'],
    status_code = status.HTTP_200_OK,
    response_model = client_schema.Client,
    dependencies = [Depends(get_db)]
)
def get_client(
    client_id: int = Path (
        ...,
        gt=0
    )
):
    return client_service.get_client(client_id)


@router.put (
    '/{client_id}',
    tags = ['client'],
    status_code = status.HTTP_200_OK,
    response_model = client_schema.Client,
    dependencies = [Depends(get_db)]
)
def update_client(
    client_id: int = Path (
        ...,
        gt=0
    ),
    client: client_schema.Client = Body(...)
):
    return client_service.update_client(client_id, 
        full_name = client.full_name, 
        email = client.email, 
        phone = client.phone, 
        address = client.address, 
        city = client.city)


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
    )
):
    return client_service.delete_client(client_id)

