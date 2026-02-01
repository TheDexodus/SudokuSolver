from src.cell.constant_cell import ConstantCell
from src.coordinate.ordinal_coordinate import OrdinalCoordinate
from src.coordinate.two_dimensional_coordinate import TwoDimensionalCoordinate
from src.field.line_builder import LineBuilder
from src.field.rectangle_field import RectangleField


def get_ascending_rectangle_field():
    rectangle_field = RectangleField((3, 3))

    for x in range(1, 10):
        for y in range(1, 10):
            grid_x, grid_y = (x - 1) // 3 + 1, (y - 1) // 3 + 1
            cell_x, cell_y = ((x - 1) % 3) + 1, ((y - 1) % 3) + 1

            grid = rectangle_field.get_grid(TwoDimensionalCoordinate(grid_x, grid_y))
            grid.set_cell(TwoDimensionalCoordinate(cell_x, cell_y), ConstantCell(x + y))

    return rectangle_field


def test_vertical_line_build():
    rectangle_field = get_ascending_rectangle_field()

    for j in range(1, 10):
        line = LineBuilder.build_column_line(rectangle_field, j)
        assert line.get_count_cells() == 9

        for i in range(1, 10):
            assert line.get_cell(OrdinalCoordinate(i)).get_value() == i + j


def test_horizontal_line_build():
    rectangle_field = get_ascending_rectangle_field()

    for j in range(1, 10):
        line = LineBuilder.build_row_line(rectangle_field, j)
        assert line.get_count_cells() == 9

        for i in range(1, 10):
            assert line.get_cell(OrdinalCoordinate(i)).get_value() == i + j