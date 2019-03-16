import pytest


@pytest.mark.usefixtures('db')
def test_some_obj(some_obj):
    assert some_obj == {}
