from mongoengine import Document, StringField

from .constants import ASSETS_BY_TYPE_CHOICES


class Asset(Document):
    """The source of truth."""

    type = StringField(choices=ASSETS_BY_TYPE_CHOICES, required=True)
    symbol = StringField(max_length=10, required=True, unique_with=['exchange'])

    def __str__(self):
        return f'{self.symbol} | {self.type}'
