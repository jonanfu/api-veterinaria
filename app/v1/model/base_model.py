import peewee

from app.v1.utils.db import db

class BaseModel(peewee.Model):

    class Meta:
        database = db
