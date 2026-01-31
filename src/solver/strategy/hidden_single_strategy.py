from src.cell.candidate_cell import CandidateCell
from src.cell.constant_cell import ConstantCell
from src.cell.empty_cell import EmptyCell
from src.coordinate.two_dimensional_coordinate import TwoDimensionalCoordinate
from src.field.line_builder import LineBuilder
from src.field.rectangle_field import RectangleField
from src.solver.strategy.strategy import Strategy

'''
    Стратегия: "Скрытая одиночка"
    Идея: Если в рамках одного CellRepository только в одном месте можно поставить цифру - ставим)
    Пример: 
    X 1 2 3   4 5 6   7 8 9
  Y +-------+-------+-------+
  1 |   2   | 4 5 6 | 7 8 9 |
  2 | 2 1 3 | 6 4 5 | 9 7 8 |

    Тройку можно поставить в двух ячейках([1, 1] и [1, 3]).
    Но так как тройка на [3, 2] перекрывает [1, 3], мы можем поставить тройку только в [1, 1]
'''
class HiddenSingleStrategy(Strategy):
    def apply(self, field: RectangleField) -> tuple[RectangleField, bool]:
        field, has_updates_for_grid = self._apply_grid(field)
        field, has_updates_for_horizontal_line = self._apply_horizontal_line(field)
        field, has_updates_for_vertical_line = self._apply_vertical_line(field)

        return field, has_updates_for_grid or has_updates_for_horizontal_line or has_updates_for_vertical_line

    def _apply_horizontal_line(self, field: RectangleField) -> tuple[RectangleField, bool]:
        has_changes = False

        for order, line in enumerate(LineBuilder.build_all_horizontal_lines(field), 1):
            grid_y = (order - 1) // field.get_size()[1] + 1
            cell_y = (order - 1) % field.get_size()[1] + 1

            for line_coordinate, cell in line:
                grid_x = (line_coordinate.get_order() - 1) // field.get_size()[0] + 1
                cell_x = (line_coordinate.get_order() - 1) % field.get_size()[0] + 1

                grid = field.get_grid(TwoDimensionalCoordinate(grid_x, grid_y))
                cell_coordinate = TwoDimensionalCoordinate(cell_x, cell_y)

                if not isinstance(cell, CandidateCell):
                    continue

                for possible_value in cell.possible_values:
                    hidden_single = True

                    for another_cell_coordinate, another_cell in line:
                        if another_cell_coordinate == line_coordinate:
                            continue

                        if isinstance(another_cell, CandidateCell) and possible_value in another_cell.possible_values:
                            hidden_single = False
                            break

                        if possible_value == another_cell.get_value() or isinstance(another_cell, EmptyCell):
                            hidden_single = False
                            break

                    if hidden_single:
                        grid.set_cell(cell_coordinate, ConstantCell(possible_value))
                        has_changes = True
                        break

        return field, has_changes

    def _apply_vertical_line(self, field: RectangleField) -> tuple[RectangleField, bool]:
        has_changes = False

        for order, line in enumerate(LineBuilder.build_all_vertical_lines(field), 1):
            grid_x = (order - 1) // field.get_size()[0] + 1
            cell_x = (order - 1) % field.get_size()[0] + 1

            for line_coordinate, cell in line:
                grid_y = (line_coordinate.get_order() - 1) // field.get_size()[1] + 1
                cell_y = (line_coordinate.get_order() - 1) % field.get_size()[1] + 1

                grid = field.get_grid(TwoDimensionalCoordinate(grid_x, grid_y))
                cell_coordinate = TwoDimensionalCoordinate(cell_x, cell_y)

                if not isinstance(cell, CandidateCell):
                    continue

                for possible_value in cell.possible_values:
                    hidden_single = True

                    for another_cell_coordinate, another_cell in line:
                        if another_cell_coordinate == line_coordinate:
                            continue

                        if isinstance(another_cell, CandidateCell) and possible_value in another_cell.possible_values:
                            hidden_single = False
                            break

                        if possible_value == another_cell.get_value() or isinstance(another_cell, EmptyCell):
                            hidden_single = False
                            break

                    if hidden_single:
                        grid.set_cell(cell_coordinate, ConstantCell(possible_value))
                        has_changes = True
                        break

        return field, has_changes

    def _apply_grid(self, field: RectangleField) -> tuple[RectangleField, bool]:
        has_changes = False

        for grid_coordinate, grid in field:
            for cell_coordinate, cell in grid:
                if not isinstance(cell, CandidateCell):
                    continue

                for possible_value in cell.possible_values:
                    hidden_single = True

                    for another_cell_coordinate, another_cell in grid:
                        if another_cell_coordinate == cell_coordinate:
                            continue

                        if isinstance(another_cell, CandidateCell) and possible_value in another_cell.possible_values:
                            hidden_single = False
                            break

                        if possible_value == another_cell.get_value() or isinstance(another_cell, EmptyCell):
                            hidden_single = False
                            break

                    if hidden_single:
                        grid.set_cell(cell_coordinate, ConstantCell(possible_value))
                        has_changes = True
                        break

        return field, has_changes