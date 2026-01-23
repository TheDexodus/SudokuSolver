from src.cell.CellInteface import CellInterface
from src.repository.CellRepositoryInterface import CellRepositoryInterface
from src.grid.GridInterface import GridInterface
from src.unit.Coordinate import Coordinate


class Grid(GridInterface, CellRepositoryInterface):
    size: tuple[int, int]
    cells: dict[tuple[int, int], CellInterface | None]

    def __init__(self, size: tuple[int, int]):
        self.size = size
        self.cells = {}



    def get_size(self) -> tuple[int, int]:
        return self.size

    def get_cell(self, coordinate: Coordinate) -> CellInterface | None:
        if coordinate.to_tuple() in self.cells:
            return self.cells[*coordinate]

        if not coordinate.in_bounds(Coordinate(1, 1), Coordinate.from_tuple(self.size)):
            raise IndexError("Coordinate out of bounds")

        return None

    def get_cells(self) -> list[CellInterface | None]:
        return list(self.cells.values())

    def get_max_count_cells(self) -> int:
        return self.size[0] * self.size[1]

    def set_cell(self, coordinate: Coordinate, cell: CellInterface) -> None:
        old_cell = self.get_cell(coordinate)

        if old_cell is not None and not old_cell.can_be_replaced():
            raise RuntimeError("Cell already set const value")

        self.cells[*coordinate] = cell

    def check_correct(self) -> bool:
        count_values = {}

        for value in self.cells.values():
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
        if len(self.cells) != self.size[0] * self.size[1]:
            return False

        for cell in self.cells.values():
            if cell is None:
                return False

        return self.check_correct()