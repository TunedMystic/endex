import os

DB_NAME = os.environ.get('POSTGRES_DB')
DB_USER = os.environ.get('POSTGRES_USER')
DB_PASS = os.environ.get('POSTGRES_PASSWORD')
DB_HOST = os.environ.get('POSTGRES_HOST')
DB_PORT = int(os.environ.get('POSTGRES_PORT'))



# from get_secret import get

# DB_NAME = get('POSTGRES_DB')
# DB_USER = get('POSTGRES_USER')
# DB_PASS = get('POSTGRES_PASSWORD')
# DB_HOST = get('POSTGRES_HOST')
# DB_PORT = get('POSTGRES_PORT', to_type=int)

