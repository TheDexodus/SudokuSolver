from src.cell.CellInteface import CellInterface
from src.repository.CellRepositoryInterface import CellRepositoryInterface
from src.line.LineInterface import LineInterface


class Line(LineInterface, CellRepositoryInterface):
    cells: dict[int, CellInterface | None]
    count_cells: int

    def __init__(self, count_cells: int):
        self.count_cells = count_cells
        self.cells = {}

    def get_max_count_cells(self) -> int:
        return self.count_cells

    def get_cell(self, position: int) -> CellInterface | None:
        if position in self.cells:
            return self.cells[position]

        if 1 <= position <= self.count_cells:
            return None

        raise IndexError("Position out of range")

    def get_cells(self) -> list[CellInterface | None]:
        return list(self.cells.values())

    def set_cell(self, position: int, cell: CellInterface | None) -> None:
        if 1 <= position <= self.count_cells:
            self.cells[position] = cell
            return

        raise IndexError("Position out of range")

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
        if len(self.cells) != self.count_cells:
            return False

        for value in self.cells.values():
            if value is None:
                return False

        return self.check_correct()

    def __str__(self):
        result = "["

        for cell in self.cells.values():
            result += ("' '" if cell is None else str(cell)) + ", "

        return result[:-2] + "]"

    def __repr__(self):
        return str(self)