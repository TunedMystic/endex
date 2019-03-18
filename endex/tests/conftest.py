import pytest

from endex import cx
from endex.settings import TEST_DB_CONFIG
from endex.utils import sqlutils

from .factories import etf_factory, stock_factory


@pytest.fixture(scope='function')
def connection():
    """
    This fixture returns a connection to the test database.
    Tables are created before the connection is returned.
    Returns:
        psycopg2.connection: A connection to the test database.
    """
    conn = cx.get(TEST_DB_CONFIG)
    sqlutils.create_tables(conn)
    yield conn
    conn.close()


@pytest.fixture(scope='function')
def cursor(connection):
    """
    This fixture returns a cursor from the test database connection.
    Args:
        connection: The 'connection' fixture.
    Returns:
        psycopg2.cursor: A cursor from the database connection.
    """
    cursor = connection.cursor()
    yield cursor
    connection.rollback()


@pytest.fixture
def exchanges(connection):
    sqlutils.load_fixture(connection, 'exchange.sql')


@pytest.fixture
def marketindexes(connection):
    sqlutils.load_fixture(connection, 'marketindex.sql')


@pytest.fixture
def fixtures(connection):
    """
    This fixture loads all sql fixtures into the test database.
    Args:
        connection: The 'connection' fuxture.
    """
    sqlutils.load_all_fixtures(connection)


@pytest.fixture
def stocks(connection, fixtures):
    """
    This fixture generates and inserts stocks into the test database.
    Args:
        connection: The 'connection' fixture.
        fixtures: The 'fixtures' fixture.
    """
    stock_factory(connection, 10)


@pytest.fixture
def etfs(connection, fixtures):
    """
    This fixture generates and inserts etfs into the test database.
    Args:
        connection: The 'connection' fixture.
        fixtures: The 'fixtures' fixture.
    """
    etf_factory(connection, 10)
