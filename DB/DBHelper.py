from flask_peewee.db import Database


class DBHelper:
    db = None

    def __init__(self, app):
        self.db = Database(app)
