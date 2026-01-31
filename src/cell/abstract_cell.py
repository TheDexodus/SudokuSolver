from abc import ABC

from src.cell.cell import Cell


class AbstractCell(Cell, ABC):
    def __str__(self):
        if self.get_value() is None:
            return " "

        if self.get_value() > 9:
            return chr(ord("A") + self.get_value() - 10)

        return str(self.get_value())

    def __eq__(self, other: "Cell") -> bool:
        return self.__class__ == other.__class__ and self.get_value() == other.get_value()