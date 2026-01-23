from abc import ABC, abstractmethod

from src.grid.GridInterface import GridInterface
from src.line.LineInterface import LineInterface
from src.unit.Coordinate import Coordinate


class FieldInterface(ABC):
    @abstractmethod
    def get_size(self) -> tuple[int, int]:
        pass

    @abstractmethod
    def get_grid(self, coordinate: Coordinate) -> GridInterface:
        pass

    @abstractmethod
    def get_vertical_line(self, number: int) -> LineInterface:
        pass

    @abstractmethod
    def get_horizontal_line(self, number: int) -> LineInterface:
        pass

    @abstractmethod
    def check_correct(self) -> bool:
        pass

    @abstractmethod
    def check_final(self) -> bool:
        pass

    @abstractmethod
    def clone(self) -> "FieldInterface":
        pass

    @abstractmethod
    def __str__(self):
        pass