import email
from fastapi import HTTPException, status

from app.v1.schema import client_schema
from app.v1.model.client_model import Client as ClientModel

def create_client(client: client_schema.ClientCreate):
    db_client = ClientModel(
        full_name = client.full_name,
        phone = client.phone,
        address = client.address,
        identification_card = client.identification_card,
        email = client.email,
        city = client.city

    )

    db_client.save()

    return client_schema.Client(
        id = db_client.id,
        full_name = db_client.phone,
        phone = db_client.phone,
        address = db_client.address,
        identification_card = db_client.identification_card,
        email = db_client.email,
        city = db_client.city
        
    )

def get_clients():
    
    clients = ClientModel.select().order_by(ClientModel.id.desc())

    list_clients = []
    for client in clients:
        list_clients.append(
            client_schema.Client(
                id = client.id,
                full_name = client.full_name,
                phone = client.phone,
                address = client.address,
                identification_card = client.identification_card,
                email = client.email,
                city = client.city
            )
        )

    return list_clients


def get_client(client_id: int):
    client = ClientModel.filter(ClientModel.id == client_id).first()

    if not client:
        raise HTTPException(
            status_code = status.HTTP_404_NOT_FOUND,
            detail = "Client not found"
        )

    return client_schema.Client(
        id = client.id,
        full_name = client.full_name,
        phone = client.phone,
        address = client.address,
        identification_card = client.identification_card,
        email = client.email,
        city = client.city

    )


def update_client(client_id: int, 
    full_name: str = None,
    phone: str = None,
    address: str = None,
    identification_card: str = None,
    email: str = None,
    city: str = None
    ):

    client = ClientModel.filter(ClientModel.id == client_id).first()

    if not client:
        raise HTTPException(
            status_code = status.HTTP_404_NOT_FOUND,
            detail = 'Client not found'
        )

    client.full_name = full_name or client.full_name
    client.phone = phone or client.phone
    client.address = address or client.address
    client.identification_card = identification_card or client.identification_card
    client.email = email or client.email
    client.city = city or client.city

    client.save()

    return client_schema.Client(
        id = client.id,
        full_name = client.full_name,
        phone = client.phone,
        address = client.address,
        identification_card = client.identification_card,
        email = client.email,
        city = client.city
    )

def delete_client(client_id: int):
    client = ClientModel.filter(ClientModel.id == client_id).first()

    if not client:
        raise HTTPException(
            status_code = status.HTTP_404_NOT_FOUND,
            detail = 'Client not found'
        )

    client.delete_instance()
    

