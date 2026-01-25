from src.cell.cell import Cell


class AbstractCell(Cell):
    def __str__(self):
        return " " if self.get_value() is None else str(self.get_value())

    def __eq__(self, other: "Cell") -> bool:
        return self.__class__ == other.__class__ and self.get_value() == other.get_value()