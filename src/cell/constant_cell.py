from src.cell.abstract_cell import AbstractCell


class ConstantCell(AbstractCell):
    value: int

    def __init__(self, value: int):
        self.value = value

    def get_value(self) -> int:
        return self.value

    def can_be_replaced(self) -> bool:
        return False