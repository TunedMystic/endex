from mongoengine import connect

from .settings import DATABASE_HOST


def init_db():
    return connect(host=DATABASE_HOST)
