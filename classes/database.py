import peewee as pw

database = SqliteDatabase('user.db')
class BaseModel(Model):
    class Meta:
        database = database

class Language_Settings(BaseModel):
    dictionary =

