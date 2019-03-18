import datetime
from decimal import Decimal
import random

import faker
from psycopg2.extras import execute_values

from endex import constants, db


ALPHABET = 'ABCDEFGHOJKLMNOPQRSTUVWXYZ'

fake = faker.Faker()


def random_symbol():
    return ''.join(random.choice(ALPHABET) for i in range(random.choice([3, 4])))


def random_country_code():
    return constants.COUNTRIES_BY_CODE_CHOICES[
        random.randint(0, len(constants.COUNTRIES_BY_CODE_CHOICES) - 1)
    ][0]


def random_leverage():
    return random.choice(constants.ETF_LEVERAGE_BY_CODE_CHOICES)[0]


def random_cusip():
    return fake.sha1()[:9]


def random_isin(cusip):
    return random_country_code() + cusip + str(random.randint(0, 9))


def random_big_number():
    return Decimal(random.randrange(100_000_000, 8_000_000_000))


def random_percent():
    return Decimal(str(random.random())).quantize(Decimal('0.00000'))


def random_phone():
    return '-'.join(str(random.randint(100, 999)) for _ in range(3)) + str(random.randint(0, 9))


def stock_factory(conn, rows=100):
    with conn:
        with conn.cursor() as cursor:
            sql = '''
                INSERT INTO stock (
                    asset_hash,
                    symbol,
                    name,
                    description,
                    date_founded,
                    date_listed,
                    website,
                    email,
                    phone,
                    cusip,
                    isin,
                    street,
                    city,
                    zipcode,
                    country,
                    shares_float,
                    shares_outstanding,
                    held_by_institutions,
                    held_by_insiders,
                    exchange_id,
                    sector_id,
                    industry_id
                ) VALUES %s
            '''
            execute_values(cursor, sql, generate_stock_rows(conn, rows))


def generate_stock_rows(conn, rows=1):
    """
    Generate a random rows for the stock table.
    """
    data = []
    exchange_ids = db.get_ids(conn, 'exchange')
    sector_ids = db.get_ids(conn, 'sector')
    industry_ids = db.get_ids(conn, 'industry')

    for i in range(rows):
        cusip = random_cusip()
        isin = random_isin(cusip)

        data.append([
            fake.sha1(),
            random_symbol(),
            fake.company(),

            ' '.join(fake.paragraphs()),
            str(fake.date_time_between(start_date="-30y", end_date="-20y", tzinfo=datetime.timezone.utc)),
            str(fake.date_time_between(start_date="-19y", end_date="-1y", tzinfo=datetime.timezone.utc)),
            fake.url(),
            fake.email(),
            random_phone(),

            cusip,
            isin,

            fake.street_address(),
            fake.city(),
            fake.zipcode(),
            random_country_code(),

            random_big_number(),  # shares_float
            random_big_number(),  # shares_outstanding
            random_percent(),  # held by institutions
            random_percent(),  # held by insiders

            random.choice(exchange_ids),
            random.choice(sector_ids),
            random.choice(industry_ids),
        ])
    return data


def etf_factory(conn, rows=100):
    with conn:
        with conn.cursor() as cursor:
            sql = '''
                INSERT INTO etf (
                    asset_hash,
                    symbol,
                    name,
                    description,
                    date_founded,
                    date_listed,
                    website,
                    email,
                    phone,
                    cusip,
                    isin,
                    leverage,
                    total_assets,
                    exchange_id,
                    category_id,
                    issuer_id,
                    marketindex_id
                ) VALUES %s
            '''
            execute_values(cursor, sql, generate_etf_rows(conn, rows))


def generate_etf_rows(conn, rows=1):
    """
    Generate a random row for the etf table.
    """
    data = []
    exchange_ids = db.get_ids(conn, 'exchange')
    marketindex_ids = db.get_ids(conn, 'marketindex')
    category_ids = db.get_ids(conn, 'category')
    etfissuer_ids = db.get_ids(conn, 'etfissuer')

    for i in range(rows):
        cusip = random_cusip()
        isin = random_isin(cusip)

        data.append([
            fake.sha1(),
            random_symbol(),
            fake.company(),

            ' '.join(fake.paragraphs()),
            str(fake.date_time_between(start_date="-30y", end_date="-20y", tzinfo=datetime.timezone.utc)),
            str(fake.date_time_between(start_date="-19y", end_date="-1y", tzinfo=datetime.timezone.utc)),
            fake.url(),
            fake.email(),
            random_phone(),

            cusip,
            isin,

            random_leverage(),
            random_big_number(),

            random.choice(exchange_ids),
            random.choice(category_ids),
            random.choice(etfissuer_ids),
            random.choice(marketindex_ids),
        ])
    return data
