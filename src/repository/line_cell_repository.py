from src.cell.empty_cell import EmptyCell
from src.coordinate.ordinal_coordinate import OrdinalCoordinate
from src.repository.abstract_cell_repository import AbstractCellRepository


class LineCellRepository(AbstractCellRepository[OrdinalCoordinate]):
    def __init__(self, count_cells: int):
        self._cells = {}

        for i in range(1, count_cells + 1):
            self._cells[OrdinalCoordinate(i)] = EmptyCell()

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
        for value in self._cells.values():
            if value.get_value() is None:
                return False

        return self.check_correct()

    def __str__(self):
        result = "["

        for cell in self._cells.values():
            result += ("' '" if cell is None else str(cell)) + ", "

        return result[:-2] + "]"

    def __repr__(self):
        return str(self)

    def clone(self) -> "LineCellRepository":
        new_repository = LineCellRepository(self.get_count_cells())

        for coordinate, cell in self:
            new_repository.set_cell(coordinate, cell.clone())

        return new_repository