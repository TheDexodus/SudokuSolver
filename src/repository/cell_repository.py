from abc import ABC, abstractmethod
from typing import Iterator

from src.cell.cell import Cell
from src.coordinate.coordinate import Coordinate


class CellRepository(ABC):
    @abstractmethod
    def get_cells(self) -> dict[Coordinate, Cell]:
        pass

    @abstractmethod
    def get_cell(self, coordinate: Coordinate) -> Cell:
        pass

    @abstractmethod
    def get_count_cells(self) -> int:
        pass

    @abstractmethod
    def set_cell(self, coordinate: Coordinate, cell: Cell) -> None:
        pass

    @abstractmethod
    def __iter__(self) -> Iterator[tuple[Coordinate, Cell]]:
        pass

    @abstractmethod
    def clone(self) -> "CellRepository":
        pass