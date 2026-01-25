from abc import ABC, abstractmethod

from repository.grid_cell_repository import GridCellRepository
from repository.line_cell_repository import LineCellRepository
from src.unit.coordinate import Coordinate


class Field(ABC):
    @abstractmethod
    def get_size(self) -> tuple[int, int]:
        pass

    @abstractmethod
    def get_grid(self, coordinate: Coordinate) -> GridCellRepository:
        pass

    @abstractmethod
    def get_vertical_line(self, number: int) -> LineCellRepository:
        pass

    @abstractmethod
    def get_horizontal_line(self, number: int) -> LineCellRepository:
        pass

    @abstractmethod
    def check_correct(self) -> bool:
        pass

    @abstractmethod
    def check_final(self) -> bool:
        pass

    @abstractmethod
    def clone(self) -> "Field":
        pass

    @abstractmethod
    def __str__(self):
        pass