from mongoengine import (
    DateTimeField, DecimalField, Document, EmailField,
    EmbeddedDocument, EmbeddedDocumentField,
    IntField, ListField, StringField, URLField,
)

from .constants import (
    ASSETS_BY_TYPE_CHOICES,
    COUNTRIES_BY_CODE_CHOICES,
    ETF_LEVERAGE_BY_CODE_CHOICES,
    EXCHANGES_BY_NAME_CHOICES,
)


# -------------------------------------------------------------------
# ------------------ Embedded Model definitions ---------------------


class Address(EmbeddedDocument):
    """An embedded document that stores address info."""

    street = StringField()
    city = StringField()
    zipcode = StringField()
    country = StringField(max_length=2, chocies=COUNTRIES_BY_CODE_CHOICES)

    def __str__(self):
        return f'{self.street}, {self.city}, {self.country}'


class Contact(EmbeddedDocument):
    """An embedded document that stores contact info."""

    email = EmailField()
    phone = StringField()

    def __str__(self):
        return f'{self.email}, {self.phone}'


# -------------------------------------------------------------------
# ------------------ Concrete Model definitions ---------------------


class Asset(Document):
    """The Asset document represents a financial asset."""

    asset_hash = StringField()

    type = StringField(choices=ASSETS_BY_TYPE_CHOICES, required=True)
    symbol = StringField(max_length=10, required=True, unique_with=['exchange'])
    name = StringField(required=True)
    exchange = StringField(choices=EXCHANGES_BY_NAME_CHOICES)
    market_index = StringField()
    cusip = StringField(max_length=9)
    isin = StringField(max_length=12)

    description = StringField()
    website = URLField()
    date_founded = DateTimeField()
    date_listed = DateTimeField()

    sector = StringField()
    industry = StringField()
    issuer = StringField()
    category = StringField()
    tags = ListField(StringField())

    shares_float = DecimalField(max_digits=12, decimal_places=0)
    shares_outstanding = DecimalField(max_digits=12, decimal_places=0)
    held_by_institutions = DecimalField(max_digits=6, decimal_places=5)
    held_by_insiders = DecimalField(max_digits=6, decimal_places=5)

    leverage = IntField(choices=ETF_LEVERAGE_BY_CODE_CHOICES)
    total_assets = DecimalField(max_digits=12, decimal_places=0)

    address = EmbeddedDocumentField(Address)
    contact = EmbeddedDocumentField(Contact)

    meta = {'collection': 'assets'}

    def __str__(self):
        return f'{self.symbol} | {self.type}'
