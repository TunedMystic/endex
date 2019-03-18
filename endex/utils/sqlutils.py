from os import listdir

from endex import settings


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


def load_fixture(conn, filename):
    load_sql(conn, f'{settings.SQL_FIXTURES_DIR}/{filename}')


def load_all_fixtures(conn):
    for fixture_file in listdir(settings.SQL_FIXTURES_DIR):
        load_fixture(conn, fixture_file)


def run_migration(conn, filename):
    load_sql(conn, f'{settings.SQL_MIGRATIONS_DIR}/{filename}')


def create_tables(conn):
    load_sql(conn, f'{settings.SQL_SETUP_DIR}/create_tables.sql')


def create_test_database(conn):
    CONFIG = settings.TEST_DB_CONFIG
    conn.autocommit = True

    cursor = conn.cursor()
    cursor.execute(f'DROP DATABASE IF EXISTS {CONFIG["dbname"]};')
    cursor.execute(f'CREATE DATABASE {CONFIG["dbname"]};')
    cursor.execute(f'GRANT ALL PRIVILEGES ON DATABASE {CONFIG["dbname"]} to {CONFIG["user"]};')
