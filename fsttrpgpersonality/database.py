from peewee import Model, SqliteDatabase, CharField
from fsttrpgtables.db import DBManager as TableManager

personality_db = SqliteDatabase('personalities.db')


class Personality(Model):
    character_name = CharField(unique=True)


class DBManager(object):
    def __init__(self):
        super(DBManager, self).__init__()
        self.tables_db_mgr = TableManager()
        personality_db.connect()
        personality_db.create_tables([Personality], True)
        self.personality_db = personality_db

    def __del__(self):
        personality_db.close()
