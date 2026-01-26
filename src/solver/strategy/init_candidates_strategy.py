from src.cell.candidate_cell import CandidateCell
from src.cell.empty_cell import EmptyCell
from src.field.rectangle_field import RectangleField
from src.solver.strategy.strategy import Strategy


class InitialCandidatesStrategy(Strategy):
    def apply(self, field: RectangleField) -> tuple[RectangleField, bool]:
        have_updates = False

        for grid_coordinate, grid in field:
            for cell_coordinate, cell in grid:
                if isinstance(cell, EmptyCell):
                    have_updates = True
                    grid.set_cell(cell_coordinate, CandidateCell(self._get_possible_values(field)))

        return field, have_updates

    def _get_possible_values(self, field: RectangleField) -> list[int]:
        possible_values = []

        for possible_value in range(1, field.get_size()[0] * field.get_size()[1] + 1):
            possible_values.append(possible_value)

        return possible_values