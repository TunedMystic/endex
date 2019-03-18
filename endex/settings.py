import os


def get(key, default=None, to_type=None):
    """
    Get environment variable, and optionally cast to a given type.
    Args:
        key (str):          The env variable to get.
        default (any):      The default value if env variable is
                            not found.
        to_type (callable): A callable to cast the env variable to
                            a specific type.
    Returns:
        value (any | None): The value of the environment variable.
    """
    value = os.environ.get(key, default)
    if callable(to_type):
        if to_type == bool:
            value = value.lower() in ['true']
        else:
            value = to_type(value)
    return value

# -------------------------------------------------------------------


SQL_FIXTURES_DIR = get('SQL_FIXTURES_DIR')
SQL_MIGRATIONS_DIR = get('SQL_MIGRATIONS_DIR')
SQL_SETUP_DIR = get('SQL_SETUP_DIR')

DB_CONFIG = {
    'dbname': get('POSTGRES_DB'),
    'user': get('POSTGRES_USER'),
    'password': get('POSTGRES_PASSWORD'),
    'host': get('POSTGRES_HOST'),
    'port': get('POSTGRES_PORT', '5432', to_type=int),
}

TEST_DB_CONFIG = {**DB_CONFIG}
TEST_DB_CONFIG['dbname'] = get('POSTGRES_DB_TEST')
