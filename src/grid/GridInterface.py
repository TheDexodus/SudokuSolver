from abc import abstractmethod

from src.cell.CellInteface import CellInterface
from src.repository.CellRepositoryInterface import CellRepositoryInterface
from src.unit.Coordinate import Coordinate


class GridInterface(CellRepositoryInterface):
    @abstractmethod
    def get_size(self) -> tuple[int, int]:
        pass

    @abstractmethod
    def get_cell(self, coordinate: Coordinate) -> CellInterface | None:
        pass

    @abstractmethod
    def set_cell(self, coordinate: Coordinate, cell: CellInterface) -> None:
        pass

    @abstractmethod
    def check_correct(self) -> bool:
        pass

    @abstractmethod
    def check_final(self) -> bool:
        pass