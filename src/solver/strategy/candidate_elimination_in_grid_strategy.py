from src.cell.candidate_cell import CandidateCell
from src.cell.constant_cell import ConstantCell
from src.coordinate.ordinal_coordinate import OrdinalCoordinate
from src.coordinate.two_dimensional_coordinate import TwoDimensionalCoordinate
from src.field.line_builder import LineBuilder
from src.field.rectangle_field import RectangleField
from src.repository.cell_repository import CellRepository
from src.solver.strategy.strategy import Strategy


class CandidateEliminationInGridStrategy(Strategy):
    def apply(self, field: RectangleField) -> tuple[RectangleField, bool]:
        have_updates = False

        for grid_coordinate, grid in field:
            grid, have_updates_in_repository = self._apply_for_cell_repository(grid)
            have_updates = have_updates or have_updates_in_repository

        for order, line in enumerate(LineBuilder.build_all_horizontal_lines(field), 1):
            line, have_updates_in_repository = self._apply_for_cell_repository(line)

            if have_updates_in_repository:
                LineBuilder.insert_horizontal_line(field, line, order)
                have_updates = True

        for order, line in enumerate(LineBuilder.build_all_vertical_lines(field), 1):
            line, have_updates_in_repository = self._apply_for_cell_repository(line)

            if have_updates_in_repository:
                LineBuilder.insert_vertical_line(field, line, order)
                have_updates = True

        return field, have_updates

    def _apply_for_cell_repository(self, cell_repository: CellRepository) -> tuple[CellRepository, bool]:
        have_updates = False
        candidate_cell = CandidateCell([])

        for coordinate, cell in cell_repository:
            if isinstance(cell, ConstantCell):
                candidate_cell.add_possible_value(cell.get_value())

        for coordinate, cell in cell_repository:
            if isinstance(cell, CandidateCell):
                new_candidate_cell = cell - candidate_cell
                if not new_candidate_cell.same_possible_values(cell):
                    have_updates = True
                    cell_repository.set_cell(coordinate, new_candidate_cell)

        return cell_repository, have_updates