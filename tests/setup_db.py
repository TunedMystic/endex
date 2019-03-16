import psycopg2

from endex.settings import (
    DB_NAME,
    DB_USER,
    DB_PASS,
    DB_HOST,
    DB_PORT,
)

CONFIG = {
    'dbname': DB_NAME,
    'user': DB_USER,
    'password': DB_PASS,
    'host': DB_HOST,
    'port': DB_PORT,
}

# Make database connection, and get cursor.
conn = psycopg2.connect(**CONFIG)
conn.autocommit = True
cursor = conn.cursor()

# Execute sql script to create tables.
cursor.execute(open('/app/db/tables.sql', 'r').read())
