import pytest
from stuff.accum import Accumulater


@pytest.fixture
def accum():
    return Accumulater()

def test_accum_init(accum):
    assert accum._count == 0

def test_accum_add(accum):
    accum.add()
    assert accum._count == 1

def test_accum_add3(accum):
    accum.add(3)
    assert accum._count == 3

def test_accum_add_twice(accum):
    accum.add()
    accum.add()
    assert accum._count == 2

def test_accum_cannot_set_count(accum):
    with pytest.raises(AttributeError, match="can't set attribute") as e:
        accum.count = 10



