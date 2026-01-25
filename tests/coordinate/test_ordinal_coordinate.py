import pytest

from src.coordinate.ordinal_coordinate import OrdinalCoordinate


def test_get_id():
    coordinate = OrdinalCoordinate(5)

    assert coordinate.get_id() == "5"


def test_get_order():
    coordinate = OrdinalCoordinate(10)

    assert coordinate.get_order() == 10


def test_from_id():
    coordinate = OrdinalCoordinate.from_id("7")

    assert isinstance(coordinate, OrdinalCoordinate)
    assert coordinate.get_order() == 7
    assert coordinate.get_id() == "7"


def test_equals():
    assert OrdinalCoordinate(13) == OrdinalCoordinate(13)


def test_hash():
    assert hash(OrdinalCoordinate(10)) == hash(OrdinalCoordinate(10))