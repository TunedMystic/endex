from endex import cx
from endex.utils import sqlutils
from endex.utils.factories import etf_factory, stock_factory


def setup():
    print('[setup] get connection')
    conn = cx.get()

    print('[setup] create tables')
    sqlutils.create_tables(conn)

    print('[setup] load all fixtures')
    sqlutils.load_all_fixtures(conn)

    print('[setup] seed db')
    etf_factory(conn, 137)
    stock_factory(conn, 284)

    print('[setup] create test database')
    sqlutils.create_test_database(conn)


setup()
