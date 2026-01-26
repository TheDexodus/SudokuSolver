from abc import ABC, abstractmethod
from typing import Iterator

from src.coordinate.two_dimensional_coordinate import TwoDimensionalCoordinate
from src.repository.grid_cell_repository import GridCellRepository


class Field(ABC):
    @abstractmethod
    def get_size(self) -> tuple[int, int]:
        pass

    @abstractmethod
    def get_grid(self, coordinate: TwoDimensionalCoordinate) -> GridCellRepository:
        pass

    @abstractmethod
    def __str__(self):
        pass

    @abstractmethod
    def __iter__(self) -> Iterator[GridCellRepository]:
        pass