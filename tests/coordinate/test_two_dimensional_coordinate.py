import pytest

from src.coordinate.two_dimensional_coordinate import TwoDimensionalCoordinate


def test_get_id():
    coordinate = TwoDimensionalCoordinate(10, 20)

    assert coordinate.get_id() == "10,20"


def test_get_x():
    coordinate = TwoDimensionalCoordinate(10, 20)

    assert coordinate.get_x() == 10


def test_get_y():
    coordinate = TwoDimensionalCoordinate(10, 20)

    assert coordinate.get_y() == 20


def test_from_id():
    coordinate = TwoDimensionalCoordinate.from_id("10,20")

    assert coordinate.get_id() == "10,20"
    assert coordinate.get_x() == 10
    assert coordinate.get_y() == 20

def test_equals():
    assert TwoDimensionalCoordinate(10, 20) == TwoDimensionalCoordinate(10, 20)


def test_hash():
    assert hash(TwoDimensionalCoordinate(10, 20)) == hash(TwoDimensionalCoordinate(10, 20))