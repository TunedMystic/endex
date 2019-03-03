import mongoengine
import pytest


@pytest.fixture(scope='function')
def mongo():
    db = mongoengine.connect('testdb', host='mongomock://localhost')
    yield db
    db.drop_database('testdb')
    db.close()
