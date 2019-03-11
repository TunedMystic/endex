from peewee import (Model, CharField, DateField,
                    DecimalField, ForeignKeyField,
                    IntegerField, TextField)

from .constants import (COUNTRIES_BY_CODE_CHOICES,
                        ETF_LEVERAGE_BY_CODE_CHOICES,
                        ETF_LEVERAGE_NONE)
from .db import get_db


database = get_db()


class BaseModel(Model):
    class Meta:
        database = database


class SimpleModel(BaseModel):
    name = CharField()

    def __str__(self):
        return self.name


class Exchange(SimpleModel):
    pass


class MarketIndex(SimpleModel):
    pass


class Category(SimpleModel):
    pass


class EtfIssuer(SimpleModel):
    pass


class Sector(SimpleModel):
    pass


class Industry(SimpleModel):
    pass


class AssetBase(SimpleModel):
    """
    Base class for a financial Asset.
    """

    # asset_hash = CharField(max_length=40)

    symbol = CharField(max_length=10)
    exchange = ForeignKeyField(Exchange, null=True)
    description = TextField(null=True)
    date_founded = DateField(null=True)
    date_listed = DateField(null=True)
    website = DateField(null=True)
    email = CharField(null=True)
    phone = CharField(null=True)

    def __str__(self):
        return self.symbol


class IdentifierMixin(BaseModel):
    cusip = CharField(max_length=9, null=True)
    isin = CharField(max_length=12, null=True)


class AddressMixin(BaseModel):
    street = CharField(null=True)
    city = CharField(null=True)
    zipcode = CharField(null=True)
    country = CharField(max_length=2, choices=COUNTRIES_BY_CODE_CHOICES, null=True)


class Stock(AssetBase, IdentifierMixin, AddressMixin):
    sector = ForeignKeyField(Sector, backref='stocks', null=True)
    industry = ForeignKeyField(Industry, backref='stocks', null=True)
    shares_float = DecimalField(max_digits=12, decimal_places=0, null=True)
    shares_outstanding = DecimalField(max_digits=12, decimal_places=0, null=True)
    held_by_institutions = DecimalField(max_digits=6, decimal_places=5, null=True)
    held_by_insiders = DecimalField(max_digits=6, decimal_places=5, null=True)


class Etf(AssetBase, IdentifierMixin):
    issuer = ForeignKeyField(EtfIssuer, backref='etfs', null=True)
    category = ForeignKeyField(Category, backref='etfs', null=True)
    market_index = ForeignKeyField(MarketIndex, backref='etfs', null=True)
    leverage = IntegerField(choices=ETF_LEVERAGE_BY_CODE_CHOICES, default=ETF_LEVERAGE_NONE, null=True)
    total_assets = DecimalField(max_digits=12, decimal_places=0, null=True)


def create_tables():
    with database:
        database.create_tables([Exchange, MarketIndex, Category,
                                EtfIssuer, Sector, Industry, Stock, Etf])
