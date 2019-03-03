import pytest

from .fixtures import mongo


@pytest.mark.usefixtures('mongo')
def test_something(mongo):
    assert 1 == 1
