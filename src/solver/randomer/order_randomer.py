from src.cell.candidate_cell import CandidateCell
from src.cell.constant_cell import ConstantCell
from src.field.field import Field
from src.solver.randomer.randomer import Randomer


class OrderRandomer(Randomer):
    _history: list[tuple[Field, int]]

    def reset(self):
        self._history = []

    def next(self, new_field: Field|None = None) -> Field|None:
        i = 0

        if new_field is not None:
            self._history.append((new_field.clone(), 0))

        if len(self._history) == 0:
            return None

        previous_field, candidate_selector = self._history[-1]
        field = previous_field.clone()

        for grid_coordinate, grid in field:
            for cell_coordinate, cell in grid:
                if isinstance(cell, CandidateCell):
                    for possible_value in cell.get_possible_values():
                        if i == candidate_selector:
                            self._history[-1] = field.clone(), candidate_selector + 1
                            grid.set_cell(cell_coordinate, ConstantCell(possible_value))
                            return field
                        i += 1

        self._history = self._history[:-1]

        if len(self._history) == 0:
            return None

        return self.next()