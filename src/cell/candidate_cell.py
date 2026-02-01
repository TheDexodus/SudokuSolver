from typing import Union

from src.cell.abstract_cell import AbstractCell
from src.cell.cell import Cell


class CandidateCell(AbstractCell):
    _possible_values: list[int]

    def __init__(self, possible_values: list[int] = None) -> None:
        super().__init__()
        self._possible_values = [] if possible_values is None else possible_values

    def get_value(self) -> int | None:
        return None

    def can_be_replaced(self) -> bool:
        return True

    def get_possible_values(self) -> list[int]:
        return self._possible_values

    def add_possible_value(self, possible_value: int) -> None:
        if possible_value not in self._possible_values:
            self._possible_values.append(possible_value)

    def is_possible_value(self, possible_value: int) -> bool:
        return possible_value in self._possible_values

    def __and__(self, other: "CandidateCell") -> "CandidateCell":
        new_cell = CandidateCell()

        for possible_value in list(set(self.get_possible_values()) & set(other.get_possible_values())):
            new_cell.add_possible_value(possible_value)

        return new_cell

    def __sub__(self, other: Union["CandidateCell", int]) -> "CandidateCell":
        if isinstance(other, int):
            return CandidateCell(list(set(self.get_possible_values()) - {other}))

        if isinstance(other, CandidateCell):
            new_cell = CandidateCell()

            for possible_value in list(set(self.get_possible_values()) - set(other.get_possible_values())):
                new_cell.add_possible_value(possible_value)

            return new_cell

        raise RuntimeError(f"Candidate cell can't be subtracted from other cell of type {other.__class__.__name__}")

    def clone(self) -> "CandidateCell":
        return CandidateCell(self._possible_values)

    def same_possible_values(self, candidate_cell: "CandidateCell") -> bool:
        if len(self._possible_values) != len(candidate_cell._possible_values):
            return False

        for possible_value in self._possible_values:
            if possible_value not in candidate_cell._possible_values:
                return False

        return True

    def __eq__(self, other: "Cell") -> bool:
        if not isinstance(other, CandidateCell):
            return False

        return self.same_possible_values(other)

    def __ne__(self, other: "Cell") -> bool:
        if not isinstance(other, CandidateCell):
            return True

        return not self.same_possible_values(other)