from src.cell.AbstractCell import AbstractCell


class EmptyCell(AbstractCell):
    def get_value(self) -> int | None:
        return None

    def can_be_replaced(self) -> bool:
        return True