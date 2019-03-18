def test_exchange_1(exchanges, cursor):
    with cursor:
        cursor.execute('SELECT COUNT(*) FROM exchange;')
        assert cursor.fetchone()[0] == 10


def test_exchange_2(exchanges, cursor):
    with cursor:
        cursor.execute('SELECT COUNT(*) FROM exchange;')
        assert cursor.fetchone()[0] == 10


def test_get_ids_for_stocks(stocks, connection):
    with connection.cursor() as cursor:
        cursor.execute('SELECT COUNT(*) FROM exchange;')
        assert cursor.fetchone()[0] == 10


def test_marketindex_1(marketindexes, cursor):
    with cursor:
        cursor.execute('SELECT x.id, x.symbol, x.name FROM marketindex x;')
        res = cursor.fetchone()
        assert res[0] is not None
        assert res[1] is not None
        assert res[2] is not None


def test_exchange_4(exchanges, cursor):
    with cursor:
        cursor.execute('SELECT COUNT(*) FROM exchange;')
        assert cursor.fetchone()[0] == 10
