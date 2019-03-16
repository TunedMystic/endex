import pytest


@pytest.fixture(scope='function')
def db():
    # db = mongoengine.connect('testdb', host='mongomock://localhost')
    db = None
    yield db
    # db.drop_database('testdb')
    # db.close()


@pytest.fixture
def some_obj():
    return {}
