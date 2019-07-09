import datetime

from peewee import *

database = SqliteDatabase('user.db')
class BaseModel(Model):
    class Meta:
        database = database

class Article(BaseModel):
    text = TextField()
    created = DateTimeField()


