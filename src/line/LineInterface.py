from abc import abstractmethod

from src.cell.CellInteface import CellInterface
from src.repository.CellRepositoryInterface import CellRepositoryInterface


class LineInterface(CellRepositoryInterface):
    @abstractmethod
    def set_cell(self, position: int, cell: CellInterface | None) -> None:
        pass

    @abstractmethod
    def get_cell(self, position: int) -> CellInterface | None:
        pass

    @abstractmethod
    def check_correct(self) -> bool:
        pass

    @abstractmethod
    def check_final(self) -> bool:
        pass