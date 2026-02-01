from typing import Iterator

from src.cell.cell import Cell
from src.coordinate.coordinate import Coordinate
from src.coordinate.two_dimensional_coordinate import TwoDimensionalCoordinate
from src.field.field import Field
from src.repository.grid_cell_repository import GridCellRepository


class RectangleField(Field):
    _size: tuple[int, int]
    _grids: dict[TwoDimensionalCoordinate, GridCellRepository]

    def __init__(self, size: tuple[int, int]) -> None:
        self._size = size
        self._grids = {}

        for y in range(1, size[1] + 1):
            for x in range(1, size[0] + 1):
                self._grids[TwoDimensionalCoordinate(x, y)] = GridCellRepository((size[1], size[0]))

    def set_cell(self, coordinate: TwoDimensionalCoordinate, cell: Cell) -> None:
        x, y = coordinate.get_col(), coordinate.get_row()
        grid_x, grid_y = (x - 1) // self._size[0] + 1, (y - 1) // self._size[1] + 1
        cell_x, cell_y = (x - 1) % self._size[0] + 1, (y - 1) % self._size[1] + 1
        grid_coordinate = TwoDimensionalCoordinate(grid_x, grid_y)
        cell_coordinate = TwoDimensionalCoordinate(cell_x, cell_y)
        self.get_grid(grid_coordinate).set_cell(cell_coordinate, cell)

    def get_size(self) -> tuple[int, int]:
        return self._size

    def get_grid(self, coordinate: TwoDimensionalCoordinate) -> GridCellRepository:
        if coordinate in self._grids:
            return self._grids[coordinate]

        raise IndexError(f"Coordinate out of bounds: Requested grid coordinate: {coordinate.get_id()}")

    def get_cell(self, coordinate: TwoDimensionalCoordinate) -> Cell | None:
        grid_col, grid_row = (coordinate.get_col() - 1) // self._size[0] + 1, (coordinate.get_row() - 1) // self._size[1] + 1
        cell_col, cell_row = (coordinate.get_col() - 1) % self._size[0] + 1, (coordinate.get_row() - 1) % self._size[1] + 1

        return self._grids[TwoDimensionalCoordinate(grid_col, grid_row)].get_cell(TwoDimensionalCoordinate(cell_col, cell_row))

    def __str__(self) -> str:
        result = ""

        for grid_y in range(1, self._size[1] + 1):
            result += "\n+" + (("-" * (self._size[1] * 2 + 1)) + "+") * self._size[0]
            for cell_y in range(1, self._size[0] + 1):
                result += "\n"
                for grid_x in range(1, self._size[0] + 1):
                    result += "| "
                    grid = self.get_grid(TwoDimensionalCoordinate(grid_x, grid_y))

                    for cell_x in range(1, self._size[1] + 1):
                        cell = grid.get_cell(TwoDimensionalCoordinate(cell_x, cell_y))
                        result += str(" " if cell is None else str(cell)) + " "
                result += "|"
        result += "\n+" + (("-" * (self._size[1] * 2 + 1)) + "+") * self._size[0]

        return result.lstrip("\n")

    def __iter__(self) -> Iterator[tuple[TwoDimensionalCoordinate, GridCellRepository]]:
        return iter(self._grids.items())

    def clone(self) -> "RectangleField":
        field = RectangleField(self._size)

        for coordinate, grid in self:
            field._grids[coordinate] = grid.clone()

        return field

    def get_length(self) -> int:
        return self._size[0] * self._size[1]