from typing import TypeVar, Generic, Iterator

from src.coordinate.coordinate import Coordinate
from src.cell.cell import Cell
from src.repository.cell_repository import CellRepository

CoordinateT = TypeVar("CoordinateT", bound=Coordinate)

class AbstractCellRepository(CellRepository, Generic[CoordinateT]):
    _cells: dict[CoordinateT, Cell]

    def get_cells(self) -> dict[CoordinateT, Cell]:
        return self._cells

    def get_cell(self, coordinate: CoordinateT) -> Cell:
        if coordinate not in self._cells:
            raise IndexError("Coordinate out of bounds")

        return self._cells[coordinate]

    def get_count_cells(self) -> int:
        return len(self._cells)

    def set_cell(self, coordinate: CoordinateT, cell: Cell) -> None:
        if coordinate not in self._cells:
            raise IndexError("Coordinate out of bounds")

        if not self._cells[coordinate].can_be_replaced():
            raise RuntimeError("Cell cannot be replaced")

        self._cells[coordinate] = cell

    def __iter__(self) -> Iterator[tuple[Coordinate, Cell]]:
        return iter(self._cells.items())