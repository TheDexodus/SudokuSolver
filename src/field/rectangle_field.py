from typing import Iterator

from src.coordinate.two_dimensional_coordinate import TwoDimensionalCoordinate
from src.field.field import Field
from src.cell.cell import Cell
from src.repository.grid_cell_repository import GridCellRepository
from src.unit.coordinate import Coordinate


class RectangleField(Field):
    _size: tuple[int, int]
    _grids: dict[TwoDimensionalCoordinate, GridCellRepository]

    def __init__(self, size: tuple[int, int]) -> None:
        self._size = size
        self._grids = {}

        for y in range(1, size[1] + 1):
            for x in range(1, size[0] + 1):
                self._grids[TwoDimensionalCoordinate(x, y)] = GridCellRepository(size)

    def get_size(self) -> tuple[int, int]:
        return self._size

    def get_grid(self, coordinate: TwoDimensionalCoordinate) -> GridCellRepository:
        if coordinate in self._grids:
            return self._grids[coordinate]

        raise IndexError("Coordinate out of bounds")

    def get_cell(self, coordinate: Coordinate) -> Cell | None:
        x, y = (coordinate.x - 1) // self._size[0] + 1, (coordinate.y - 1) // self._size[1] + 1
        grid_x, grid_y = (coordinate.x - 1) % self._size[0] + 1, (coordinate.y - 1) % self._size[1] + 1

        return self._grids[TwoDimensionalCoordinate(x, y)].get_cell(TwoDimensionalCoordinate(grid_x, grid_y))

    def __str__(self) -> str:
        result = ""

        for y in range(1, self._size[1] + 1):
            result += "\n+" + (("-" * (self._size[0] * 2 + 1)) + "+") * self._size[0]
            for grid_y in range(1, self._size[1] + 1):
                result += "\n"
                for x in range(1, self._size[0] + 1):
                    result += "| "
                    grid = self.get_grid(TwoDimensionalCoordinate(x, y))

                    for grid_x in range(1, self._size[0] + 1):
                        cell = grid.get_cell(TwoDimensionalCoordinate(grid_x, grid_y))
                        result += str(" " if cell is None else str(cell)) + " "
                result += "|"
        result += "\n+" + (("-" * (self._size[0] * 2 + 1)) + "+") * self._size[0]

        return result.lstrip("\n")

    def __iter__(self) -> Iterator[tuple[TwoDimensionalCoordinate, GridCellRepository]]:
        return iter(self._grids.items())