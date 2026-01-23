from src.cell.ConstantCell import ConstantCell
from src.cell.CandidateCell import CandidateCell
from src.field.FieldInterface import FieldInterface
from src.grid.GridInterface import GridInterface
from src.possible.PossibleHelper import PossibleHelper
from src.solver.SolverInterface import SolverInterface
from src.unit.Coordinate import Coordinate


class RectangleSolver(SolverInterface):
    def solve(self, field: FieldInterface) -> FieldInterface:
        limit = 1000
        while not field.check_final() and limit > 0:
            self._and_possible_cells_by_grid(field)
            self._and_possible_cells_by_row(field)
            self._and_possible_cells_by_col(field)
            self._find_solo_possible_value(field)
            self._fill_uno_possible_value(field)
            limit -= 1

        return field

    def _find_solo_possible_value(self, field: FieldInterface) -> None:
        for x in range(1, field.get_size()[0] + 1):
            for y in range(1, field.get_size()[1] + 1):
                self._find_solo_possible_value_for_grid(field.get_grid(Coordinate(x, y)))

    def _find_solo_possible_value_for_grid(self, grid: GridInterface) -> None:
        for i in range(grid.get_size()[0] * grid.get_size()[1]):
            j = 0
            target_cell_coordinate = Coordinate(i % grid.get_size()[0] + 1, i // grid.get_size()[0] + 1)
            target_cell = grid.get_cell(target_cell_coordinate)

            if not isinstance(target_cell, CandidateCell):
                continue

            target_cell = target_cell.clone()

            for y in range(1, grid.get_size()[1] + 1):
                for x in range(1, grid.get_size()[0] + 1):
                    diff_cell = grid.get_cell(Coordinate(x, y))
                    if j != i and isinstance(diff_cell, CandidateCell):
                        target_cell = target_cell - diff_cell
                    j += 1

            if len(target_cell.get_possible_values()) == 1:
                grid.set_cell(target_cell_coordinate, ConstantCell(target_cell.get_possible_values()[0]))

    def _fill_uno_possible_value(self, field: FieldInterface) -> None:
        for x in range(1, field.get_size()[0] + 1):
            for y in range(1, field.get_size()[1] + 1):
                grid = field.get_grid(Coordinate(x, y))

                for grid_x in range(1, field.get_size()[0] + 1):
                    for grid_y in range(1, field.get_size()[1] + 1):
                        cell_coordinate = Coordinate(grid_x, grid_y)
                        cell = grid.get_cell(cell_coordinate)

                        if cell is not None and isinstance(cell, CandidateCell) and len(cell.get_possible_values()) == 1:
                            grid.set_cell(cell_coordinate, ConstantCell(cell.get_possible_values()[0]))

    def _and_possible_cells_by_row(self, field: FieldInterface) -> None:
        for y in range(1, field.get_size()[1] + 1):
            for grid_y in range(1, field.get_size()[1] + 1):
                line = field.get_horizontal_line((y - 1) * field.get_size()[1] + grid_y)
                possible_cell = PossibleHelper.get_possible_cell(line)

                for x in range(1, field.get_size()[0] + 1):
                    grid = field.get_grid(Coordinate(x, y))

                    for grid_x in range(1, field.get_size()[0] + 1):
                        cell_coordinate = Coordinate(grid_x, grid_y)
                        cell = grid.get_cell(cell_coordinate)

                        if cell is not None and isinstance(cell, CandidateCell):
                            grid.set_cell(cell_coordinate, cell & possible_cell)

    def _and_possible_cells_by_col(self, field: FieldInterface) -> None:
        for x in range(1, field.get_size()[0] + 1):
            for grid_x in range(1, field.get_size()[0] + 1):
                line = field.get_vertical_line((x - 1) * field.get_size()[0] + grid_x)
                possible_cell = PossibleHelper.get_possible_cell(line)

                for y in range(1, field.get_size()[1] + 1):
                    grid = field.get_grid(Coordinate(x, y))

                    for grid_y in range(1, field.get_size()[1] + 1):
                        cell_coordinate = Coordinate(grid_x, grid_y)
                        cell = grid.get_cell(cell_coordinate)

                        if cell is not None and isinstance(cell, CandidateCell):
                            grid.set_cell(cell_coordinate, cell & possible_cell)

    def _and_possible_cells_by_grid(self, field: FieldInterface) -> None:
        for y in range(1, field.get_size()[1] + 1):
            for x in range(1, field.get_size()[0] + 1):
                grid = field.get_grid(Coordinate(x, y))
                possible_cell_for_grid = PossibleHelper.get_possible_cell(grid)

                for grid_y in range(1, field.get_size()[1] + 1):
                    for grid_x in range(1, field.get_size()[0] + 1):
                        cell_coordinate = Coordinate(grid_x, grid_y)
                        cell = grid.get_cell(cell_coordinate)

                        if cell is None or cell.can_be_replaced():
                            if isinstance(cell, CandidateCell):
                                grid.set_cell(cell_coordinate, cell & possible_cell_for_grid)
                            else:
                                grid.set_cell(cell_coordinate, possible_cell_for_grid.clone())