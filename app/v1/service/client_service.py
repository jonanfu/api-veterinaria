from fastapi import HTTPException, status

from app.v1.schema import client_shema
from app.v1.model.client_model import Client as ClientModel

def create_client(client: client_shema.ClientCreate, user: user_schema.User):
    pass

def get_clients(client_id: int):
    pass

def get_client(client_id: int):
    pass

def update_client(client_id: int, client: client_shema.ClientUpdate):
    pass

def delete_client(client_id: int):
    pass
