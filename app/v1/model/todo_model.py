from datetime import datetime

from peewee import *

from app.v1.model.base_model import BaseModel
from app.v1.model.user_model import User

class Todo(BaseModel):
    title = CharField()
    created_at = DateTimeField(default=datetime.now)
    is_done = BooleanField(default=False)
    user = ForeignKeyField(User, backref="todo")
