from peewee import *

from app.v1.model.base_model import BaseModel

class User(BaseModel):
    email = CharField(unique=True, index=True)
    username = CharField(unique=True, index=True)
    password = CharField()
