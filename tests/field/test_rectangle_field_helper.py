from src.cell.constant_cell import ConstantCell
from src.coordinate.two_dimensional_coordinate import TwoDimensionalCoordinate
from src.field.rectangle_field import RectangleField
from src.field.rectangle_field_helper import RectangleFieldHelper


def test_rotate_field_clockwise():
    field = RectangleField((3, 3))

    for i in range(1, 10):
        field.set_cell(TwoDimensionalCoordinate(i, 1), ConstantCell(i))

    field = RectangleFieldHelper.rotate_field_clockwise(field)
    for i in range(1, 10):
        assert field.get_cell(TwoDimensionalCoordinate(9, i)).get_value() == i

    field = RectangleFieldHelper.rotate_field_clockwise(field)
    for i in range(1, 10):
        assert field.get_cell(TwoDimensionalCoordinate(10 - i, 9)).get_value() == i

    field = RectangleFieldHelper.rotate_field_clockwise(field)
    for i in range(1, 10):
        assert field.get_cell(TwoDimensionalCoordinate(1, 10 - i)).get_value() == i

    field = RectangleFieldHelper.rotate_field_clockwise(field)
    for i in range(1, 10):
        assert field.get_cell(TwoDimensionalCoordinate(i, 1)).get_value() == i


def test_rotate_field_counterclockwise():
    field = RectangleField((3, 3))

    for i in range(1, 10):
        field.set_cell(TwoDimensionalCoordinate(i, 1), ConstantCell(i))

    field = RectangleFieldHelper.rotate_field_counterclockwise(field)
    for i in range(1, 10):
        assert field.get_cell(TwoDimensionalCoordinate(1, 10 - i)).get_value() == i

    field = RectangleFieldHelper.rotate_field_counterclockwise(field)
    for i in range(1, 10):
        assert field.get_cell(TwoDimensionalCoordinate(10 - i, 9)).get_value() == i

    field = RectangleFieldHelper.rotate_field_counterclockwise(field)
    for i in range(1, 10):
        assert field.get_cell(TwoDimensionalCoordinate(9, i)).get_value() == i

    field = RectangleFieldHelper.rotate_field_counterclockwise(field)
    for i in range(1, 10):
        assert field.get_cell(TwoDimensionalCoordinate(i, 1)).get_value() == i


