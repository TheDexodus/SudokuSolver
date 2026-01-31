from src.cell.abstract_cell import AbstractCell


class EmptyCell(AbstractCell):
    def get_value(self) -> int | None:
        return None

    def can_be_replaced(self) -> bool:
        return True

    def clone(self) -> "EmptyCell":
        return EmptyCell()