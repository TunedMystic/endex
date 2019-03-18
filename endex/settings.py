import os


SQL_FIXTURES_DIR = '/app/db/fixtures'
SQL_SETUP_DIR = '/app/db/setup'

DB_CONFIG = {
    'dbname': os.environ.get('POSTGRES_DB'),
    'user': os.environ.get('POSTGRES_USER'),
    'password': os.environ.get('POSTGRES_PASSWORD'),
    'host': os.environ.get('POSTGRES_HOST'),
    'port': int(os.environ.get('POSTGRES_PORT')),
}

TEST_DB_CONFIG = {**DB_CONFIG}
TEST_DB_CONFIG['dbname'] = os.environ.get('POSTGRES_DB_TEST')
