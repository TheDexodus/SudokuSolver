from abc import abstractmethod

from src.cell.CellInteface import CellInterface
from src.field.FieldInterface import FieldInterface
from src.unit.Coordinate import Coordinate


class RectangleFieldInterface(FieldInterface):
    @abstractmethod
    def get_cell(self, coordinate: Coordinate) -> CellInterface | None:
        pass