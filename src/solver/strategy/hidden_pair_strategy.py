from src.cell.candidate_cell import CandidateCell
from src.coordinate.two_dimensional_coordinate import TwoDimensionalCoordinate
from src.field.line_builder import LineBuilder
from src.field.rectangle_field import RectangleField
from src.solver.strategy.strategy import Strategy

class HiddenPairStrategy(Strategy):
    """
    **Стратегия**: "Скрытая пара" (Hidden Pair)

    **Идея**:
    Если в строке или колонке число может находиться только в пределах
    одной сетки (grid), то это число нельзя размещать в других ячейках этой сетки.
    """

    def apply(self, field: RectangleField) -> tuple[RectangleField, bool]:
        has_updates = False

        for row_order, row_line in enumerate(LineBuilder.build_all_horizontal_lines(field), 1):
            for column_coordinate, cell in row_line:
                if not isinstance(cell, CandidateCell):
                    continue

                column_order = column_coordinate.get_order()

                grid_local_row_order = (row_order - 1) % field.get_size()[1] + 1

                grid_coordinate = TwoDimensionalCoordinate(
                    (column_order - 1) // field.get_size()[0] + 1,
                    (row_order - 1) // field.get_size()[1] + 1,
                )
                grid = field.get_grid(grid_coordinate)

                for possible_value in cell.get_possible_values():
                    founded_in_another_grid_possible_value = False

                    for second_column_coordinate, second_cell in row_line:
                        if not isinstance(second_cell, CandidateCell):
                            continue

                        second_column_order = second_column_coordinate.get_order()
                        second_grid_coordinate = TwoDimensionalCoordinate(
                            (second_column_order - 1) // field.get_size()[0] + 1,
                            (row_order - 1) // field.get_size()[1] + 1,
                        )

                        if second_column_coordinate == column_coordinate:
                            continue

                        if grid_coordinate == second_grid_coordinate:
                            continue

                        if possible_value in second_cell.get_possible_values():
                            founded_in_another_grid_possible_value = True
                            break

                    if not founded_in_another_grid_possible_value:
                        for remove_grid_coordinate, remove_cell in grid:
                            if not isinstance(remove_cell, CandidateCell):
                                continue

                            if remove_grid_coordinate.get_row() == grid_local_row_order:
                                continue

                            if possible_value not in remove_cell.get_possible_values():
                                continue

                            grid.set_cell(remove_grid_coordinate, remove_cell - possible_value)
                            has_updates = True

        for column_order, column_line in enumerate(LineBuilder.build_all_vertical_lines(field), 1):
            for row_coordinate, cell in column_line:
                if not isinstance(cell, CandidateCell):
                    continue

                row_order = row_coordinate.get_order()

                grid_local_column_order = (column_order - 1) % field.get_size()[0] + 1

                grid_coordinate = TwoDimensionalCoordinate(
                    (column_order - 1) // field.get_size()[0] + 1,
                    (row_order - 1) // field.get_size()[1] + 1,
                )
                grid = field.get_grid(grid_coordinate)

                for possible_value in cell.get_possible_values():
                    founded_in_another_grid_possible_value = False

                    for second_row_coordinate, second_cell in column_line:
                        if not isinstance(second_cell, CandidateCell):
                            continue

                        second_row_order = second_row_coordinate.get_order()
                        second_grid_coordinate = TwoDimensionalCoordinate(
                            (column_order - 1) // field.get_size()[0] + 1,
                            (second_row_order - 1) // field.get_size()[1] + 1,
                        )

                        if second_row_coordinate == row_coordinate:
                            continue

                        if grid_coordinate == second_grid_coordinate:
                            continue

                        if possible_value in second_cell.get_possible_values():
                            founded_in_another_grid_possible_value = True
                            break

                    if not founded_in_another_grid_possible_value:
                        for remove_grid_coordinate, remove_cell in grid:
                            if not isinstance(remove_cell, CandidateCell):
                                continue

                            if remove_grid_coordinate.get_col() == grid_local_column_order:
                                continue

                            if possible_value not in remove_cell.get_possible_values():
                                continue

                            grid.set_cell(remove_grid_coordinate, remove_cell - possible_value)
                            has_updates = True

        return field, has_updates