import datetime

from peewee import *

from app import db


class ClientUser(db.Model):
    pk = BigIntegerField()
    username = CharField()

    @property
    def serialize(self):
        data = {
            'id': self.id,
            "pk": self.pk,
            "username": self.username
        }

        return data


class Post(db.Model):
    pk = BigIntegerField()
    code = CharField()
    image_url = CharField()
    client = ForeignKeyField(ClientUser, backref="posts")
    created_at = DateTimeField(default=datetime.datetime.now)
    posted_at = DateTimeField(null=True)
    ignored_at = DateTimeField(null=True)

    @property
    def serialize(self):
        data = {
            'id': self.id,
            'pk': self.pk,
            'code': self.code,
            'image_url': self.image_url,
            'client': self.client,
            'created_at': self.created_at,
            'posted_at': self.posted_at,
            'ignored_at': self.ignored_at,
            "instagramURL": self.instagramURL
        }

        return data

    @property
    def instagramURL(self):
        return "https://www.instagram.com/{username}/p/{code}".format(username=self.client.username, code=self.code)


class User(db.Model):
    email = CharField(unique=True)
    password = CharField()
