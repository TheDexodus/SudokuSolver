from src.cell.candidate_cell import CandidateCell
from src.cell.constant_cell import ConstantCell
from src.cell.empty_cell import EmptyCell
from src.coordinate.two_dimensional_coordinate import TwoDimensionalCoordinate
from src.field.line_builder import LineBuilder
from src.field.rectangle_field import RectangleField
from src.solver.strategy.strategy import Strategy


class HiddenSingleStrategy(Strategy):
    """
        **Стратегия**: "Скрытая одиночка" (Hidden Single)

        **Идея**:
        В рамках одного CellRepository (строка / колонка / grid)
        для некоторого значения существует ровно одна ячейка,
        в которую это значение может быть поставлено.

        При этом сама ячейка может иметь несколько возможных значений,
        но рассматриваемое значение является уникальным
        для данного CellRepository.

        **Следствие**:
        Если значение может быть размещено только в одной ячейке
        CellRepository — оно обязательно должно быть поставлено
        в эту ячейку.
    """

    def apply(self, field: RectangleField) -> tuple[RectangleField, bool]:
        field, has_updates_for_grid = self._apply_grid(field)
        field, has_updates_for_horizontal_line = self._apply_horizontal_line(field)
        field, has_updates_for_vertical_line = self._apply_vertical_line(field)

        return field, has_updates_for_grid or has_updates_for_horizontal_line or has_updates_for_vertical_line

    def _apply_horizontal_line(self, field: RectangleField) -> tuple[RectangleField, bool]:
        has_changes = False

        for order, line in enumerate(LineBuilder.build_all_row_lines(field), 1):
            grid_y = (order - 1) // field.get_size()[0] + 1
            cell_y = (order - 1) % field.get_size()[0] + 1

            for line_coordinate, cell in line:
                grid_x = (line_coordinate.get_order() - 1) // field.get_size()[1] + 1
                cell_x = (line_coordinate.get_order() - 1) % field.get_size()[1] + 1

                grid = field.get_grid(TwoDimensionalCoordinate(grid_x, grid_y))
                cell_coordinate = TwoDimensionalCoordinate(cell_x, cell_y)

                if not isinstance(cell, CandidateCell):
                    continue

                for possible_value in cell._possible_values:
                    hidden_single = True

                    for another_cell_coordinate, another_cell in line:
                        if another_cell_coordinate == line_coordinate:
                            continue

                        if isinstance(another_cell, CandidateCell) and possible_value in another_cell._possible_values:
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

        for order, line in enumerate(LineBuilder.build_all_column_lines(field), 1):
            grid_x = (order - 1) // field.get_size()[1] + 1
            cell_x = (order - 1) % field.get_size()[1] + 1

            for line_coordinate, cell in line:
                grid_y = (line_coordinate.get_order() - 1) // field.get_size()[0] + 1
                cell_y = (line_coordinate.get_order() - 1) % field.get_size()[0] + 1

                grid = field.get_grid(TwoDimensionalCoordinate(grid_x, grid_y))
                cell_coordinate = TwoDimensionalCoordinate(cell_x, cell_y)

                if not isinstance(cell, CandidateCell):
                    continue

                for possible_value in cell._possible_values:
                    hidden_single = True

                    for another_cell_coordinate, another_cell in line:
                        if another_cell_coordinate == line_coordinate:
                            continue

                        if isinstance(another_cell, CandidateCell) and possible_value in another_cell._possible_values:
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

                for possible_value in cell._possible_values:
                    hidden_single = True

                    for another_cell_coordinate, another_cell in grid:
                        if another_cell_coordinate == cell_coordinate:
                            continue

                        if isinstance(another_cell, CandidateCell) and possible_value in another_cell._possible_values:
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