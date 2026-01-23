from abc import ABC, abstractmethod
from typing import Union

from src.cell.CellInteface import CellInterface
from src.coordinate.CoordinateInterface import CoordinateInterface


class CellRepositoryInterface(ABC):
    @abstractmethod
    def get_cells(self) -> dict[CoordinateInterface, CellInterface]:
        pass

    @abstractmethod
    def get_cell(self, coordinate: CoordinateInterface) -> CellInterface:
        pass

    @abstractmethod
    def get_count_cells(self) -> int:
        pass