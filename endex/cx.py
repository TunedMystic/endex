from contextlib import contextmanager
import logging

import psycopg2
from psycopg2 import pool

from endex import settings


logger = logging.getLogger(__name__)

connection_pool = None


def init(config=None):
    global connection_pool
    if not config:
        config = settings.DB_CONFIG
    connection_pool = pool.SimpleConnectionPool(1, 10, **config)


def get(config=None):
    if not config:
        config = settings.DB_CONFIG
    return psycopg2.connect(**config)


def _get_conn():
    conn = connection_pool.getconn()
    return conn, lambda x: connection_pool.putconn(x)


@contextmanager
def _quick_cursor():
    """
    Create a quick cursor.
    Ref: https://github.com/psycopg/psycopg2/pull/367#issuecomment-241582921
    """
    try:
        conn = connection_pool.getconn()
        with conn:
            with conn.cursor() as cursor:
                yield cursor
    except Exception as e:
        logging.error(f'[quick_cursor] {str(e)}')
        raise e
    finally:
        connection_pool.putconn(conn)
