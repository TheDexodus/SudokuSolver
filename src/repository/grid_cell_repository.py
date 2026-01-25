from src.cell.empty_cell import EmptyCell
from src.coordinate.two_dimensional_coordinate import TwoDimensionalCoordinate
from src.repository.abstract_cell_repository import AbstractCellRepository
from src.cell.cell import Cell
from src.unit.coordinate import Coordinate


class GridCellRepository(AbstractCellRepository[TwoDimensionalCoordinate]):
    _size: tuple[int, int]

    def __init__(self, size: tuple[int, int]):
        self._size = size
        self._cells = {}

        for y in range(1, size[1] + 1):
            for x in range(1, size[0] + 1):
                self._cells[TwoDimensionalCoordinate(x, y)] = EmptyCell()

    def get_size(self) -> tuple[int, int]:
        return self._size

    def get_cell(self, coordinate: Coordinate) -> Cell | None:
        if coordinate.to_tuple() in self._cells:
            return self._cells[*coordinate]

        if not coordinate.in_bounds(Coordinate(1, 1), Coordinate.from_tuple(self._size)):
            raise IndexError("Coordinate out of bounds")

        return None

    def get_cells(self) -> list[Cell | None]:
        return list(self._cells.values())

    def get_max_count_cells(self) -> int:
        return self._size[0] * self._size[1]

    def set_cell(self, coordinate: Coordinate, cell: Cell) -> None:
        old_cell = self.get_cell(coordinate)

        if old_cell is not None and not old_cell.can_be_replaced():
            raise RuntimeError("Cell already set const value")

        self._cells[*coordinate] = cell

    def check_correct(self) -> bool:
        count_values = {}

        for value in self._cells.values():
            if value is None:
                continue

            if value.get_value() not in count_values:
                count_values[value.get_value()] = 0

            count_values[value.get_value()] += 1

        for count_values in count_values.values():
            if count_values > 1:
                return False

        return True

    def check_final(self) -> bool:
        if len(self._cells) != self._size[0] * self._size[1]:
            return False

        for cell in self._cells.values():
            if cell is None:
                return False

        return self.check_correct()