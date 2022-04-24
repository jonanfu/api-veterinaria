from datetime import datetime

import peewee

from app.v1.utils.db import db
from app.v1.model.user_model import User

class Todo(peewee.Model):
    title = peewee.CharField()
    created_at = peewee.DateTimeField(default=datetime.now)
    is_done = peewee.BooleanField(default=False)
    user = peewee.ForeignKeyField(User, backref="todo")

    class Meta:
        database = db
