import os


DATABASE_HOST = os.environ.get(
    'DATABASE_HOST',
    'mongodb://mongo:password@localhost:27017/endex?authSource=admin')
