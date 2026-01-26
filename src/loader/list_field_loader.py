from math import sqrt

from src.cell.constant_cell import ConstantCell
from src.cell.empty_cell import EmptyCell
from src.coordinate.two_dimensional_coordinate import TwoDimensionalCoordinate
from src.field.rectangle_field import RectangleField
from src.loader.field_loader import FieldLoader


class ListFieldLoader(FieldLoader):
    _field: list[list[int|None]]

    def __init__(self, field: list[list[int|None]]):
        self._field = field

    def load(self) -> RectangleField:
        size = int(len(self._field[0]) ** 0.5), int(len(self._field) ** 0.5)
        field = RectangleField(size)

        for y, row in enumerate(self._field):
            grid_y = y // 3 + 1
            cell_y = y % 3 + 1

            for x, value in enumerate(row):
                grid_x = x // 3 + 1
                cell_x = x % 3 + 1

                grid = field.get_grid(TwoDimensionalCoordinate(grid_x, grid_y))
                cell = EmptyCell() if value is None or value == 0 else ConstantCell(value)
                grid.set_cell(TwoDimensionalCoordinate(cell_x, cell_y), cell)

        return field