from src.cell.empty_cell import EmptyCell
from src.coordinate.two_dimensional_coordinate import TwoDimensionalCoordinate
from src.repository.abstract_cell_repository import AbstractCellRepository


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

    def clone(self) -> "GridCellRepository":
        new_repository = GridCellRepository(self._size)

        for coordinate, cell in self:
            new_repository.set_cell(coordinate, cell.clone())

        return new_repository