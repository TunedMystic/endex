def get_ids(conn, tablename):
    """
    Return a list of ids from the table.
    Args:
        conn (psycopg2.connection): A connection to the database.
        tablename (str): The table to query.
    Returns:
        list[int]: The list of ids.
    """
    with conn:
        with conn.cursor() as cursor:
            cursor.execute(f'SELECT id FROM {tablename}')
            return [r[0] for r in cursor.fetchall()]
