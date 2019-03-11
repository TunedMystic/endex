from peewee import PostgresqlDatabase

DB_NAME = 'postgres'
DB_USER = 'postgres'
DB_PASS = 'postgres'
DB_HOST = 'localhost'
DB_PORT = 5432


def get_db():
    return PostgresqlDatabase(DB_NAME,
                              user=DB_USER,
                              password=DB_PASS,
                              host=DB_HOST,
                              port=DB_PORT)
