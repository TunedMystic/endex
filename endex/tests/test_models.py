import pytest


from endex.models import Asset


def test_asset_model_str(asset_stock):
    a = asset_stock
    assert str(a) == f'{a.symbol} | {a.type}'
    assert str(a.address) == f'{a.address.street}, {a.address.city}, {a.address.country}'
    assert str(a.contact) == f'{a.contact.email}, {a.contact.phone}'


@pytest.mark.usefixtures('mongo')
def test_asset_document_is_saved(asset_obj):
    asset_obj.save()
    assert Asset.objects.count() == 1
