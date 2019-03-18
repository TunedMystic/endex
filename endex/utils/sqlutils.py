from os import listdir

from endex.settings import SQL_FIXTURES_DIR, SQL_SETUP_DIR


def load_sql(conn, filename):
    """
    Load sql from a file.
    Args:
        conn (psycopg2.connection): A connection to the database.
        filename (str): The sql file to read.
    """
    with conn:
        with conn.cursor() as cursor:
            cursor.execute(open(filename, 'r').read())


def create_tables(conn):
    load_sql(conn, f'{SQL_SETUP_DIR}/tables.sql')


def create_test_database(conn):
    from endex.settings import TEST_DB_CONFIG
    conn.autocommit = True
    cursor = conn.cursor()
    cursor.execute(f'DROP DATABASE IF EXISTS {TEST_DB_CONFIG["dbname"]};')
    cursor.execute(f'CREATE DATABASE {TEST_DB_CONFIG["dbname"]};')
    cursor.execute(f'GRANT ALL PRIVILEGES ON DATABASE {TEST_DB_CONFIG["dbname"]} to {TEST_DB_CONFIG["user"]};')


def load_fixture(conn, filename):
    load_sql(conn, f'{SQL_FIXTURES_DIR}/{filename}')


def load_all_fixtures(conn):
    for fixture_file in listdir(SQL_FIXTURES_DIR):
        load_fixture(conn, fixture_file)
