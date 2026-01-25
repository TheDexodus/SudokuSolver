from src.cell.abstract_cell import AbstractCell


class CandidateCell(AbstractCell):
    possible_values: list[int]

    def __init__(self, possible_values: list[int] = None) -> None:
        super().__init__()
        self.possible_values = [] if possible_values is None else possible_values

    def get_value(self) -> int | None:
        return None

    def can_be_replaced(self) -> bool:
        return True

    def get_possible_values(self) -> list[int]:
        return self.possible_values

    def add_possible_value(self, possible_value: int) -> None:
        if possible_value not in self.possible_values:
            self.possible_values.append(possible_value)

    def is_possible_value(self, possible_value: int) -> bool:
        return possible_value in self.possible_values

    def __and__(self, other: "CandidateCell") -> "CandidateCell":
        new_cell = CandidateCell()

        for possible_value in list(set(self.get_possible_values()) & set(other.get_possible_values())):
            new_cell.add_possible_value(possible_value)

        return new_cell

    def __sub__(self, other: "CandidateCell") -> "CandidateCell":
        new_cell = CandidateCell()

        for possible_value in list(set(self.get_possible_values()) - set(other.get_possible_values())):
            new_cell.add_possible_value(possible_value)

        return new_cell

    def clone(self) -> "CandidateCell":
        return CandidateCell(self.possible_values)