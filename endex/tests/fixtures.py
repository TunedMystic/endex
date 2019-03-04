import mongoengine
import pytest

from endex.constants import ASSET_ETF, ASSET_STOCK
from .factories import AssetFactory


@pytest.fixture(scope='function')
def mongo():
    db = mongoengine.connect('testdb', host='mongomock://localhost')
    yield db
    db.drop_database('testdb')
    db.close()


@pytest.fixture
def asset_obj():
    return AssetFactory.build()


@pytest.fixture
def asset_etf():
    return AssetFactory.build(type=ASSET_ETF)


@pytest.fixture
def asset_stock():
    return AssetFactory.build(type=ASSET_STOCK)
