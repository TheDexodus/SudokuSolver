from src.cell.CellInteface import CellInterface


class AbstractCell(CellInterface):
    def __str__(self):
        return " " if self.get_value() is None else str(self.get_value())