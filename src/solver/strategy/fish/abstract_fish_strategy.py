from abc import ABC
from itertools import combinations

from src.cell.candidate_cell import CandidateCell
from src.coordinate.two_dimensional_coordinate import TwoDimensionalCoordinate
from src.field.line_builder import LineBuilder
from src.field.rectangle_field import RectangleField
from src.field.rectangle_field_helper import RectangleFieldHelper
from src.repository.helper.candidate_helper import CandidateHelper
from src.solver.strategy.strategy import Strategy


class AbstractFishStrategy(Strategy, ABC):
    def _apply_fish_strategy(self, field: RectangleField, n: int) -> tuple[RectangleField, bool]:
        field, has_updates_by_column = self._apply_fish_strategy_on_column(field, n)
        rotated_field, has_updates_by_row = self._apply_fish_strategy_on_column(RectangleFieldHelper.rotate_field_clockwise(field), n)

        return RectangleFieldHelper.rotate_field_counterclockwise(rotated_field), has_updates_by_column or has_updates_by_row

    def _apply_fish_strategy_on_column(self, field: RectangleField, n: int) -> tuple[RectangleField, bool]:
        exclude_cell_coordinates = set()
        count_possible_values_by_column = {}

        # Заполняем count_possible_values_by_column для того, чтобы понимать, сколько цифр встречается в каждой колонке
        for column_order, column_line in enumerate(LineBuilder.build_all_column_lines(field), 1):
            count_possible_values_by_column[column_order] = {}

            for i in range(1, field.get_size()[0] * field.get_size()[1] + 1):
                count_possible_values_by_column[column_order][i] = 0

            for possible_value in CandidateHelper.find_unique_possible_values(column_line):
                count_possible_values_by_column[column_order][possible_value] = CandidateHelper.count_candidate_cells_with_possible_value(column_line, possible_value)

        for possible_value in range(1, field.get_size()[0] * field.get_size()[1] + 1):
            possible_columns = []

            for column_order, column_line in enumerate(LineBuilder.build_all_column_lines(field), 1):
                count = count_possible_values_by_column[column_order][possible_value]

                if 1 < count <= n:
                    possible_columns.append(column_order)

            if len(possible_columns) < n:
                continue

            rows_by_column = {}

            for possible_column in possible_columns:
                candidate_cells = CandidateHelper.find_candidate_cells_with_possible_value(LineBuilder.build_column_line(field, possible_column), possible_value)
                rows_by_column[possible_column] = [coordinate.get_order() for coordinate, _ in candidate_cells]

            for unions_of_columns in combinations(possible_columns, n):
                rows_union = set().union(*(rows_by_column[c] for c in unions_of_columns))

                if len(rows_union) != n:
                    continue

                # print(f"Founded fish({n}) with number {possible_value} in columns {', '.join([str(c) for c in unions_of_columns])} and rows {', '.join([str(r) for r in rows_union])}")

                for row_order in rows_union:
                    row = LineBuilder.build_row_line(field, row_order)

                    for row_coordinate, cell in row:
                        if row_coordinate.get_order() in unions_of_columns:
                            continue

                        if not isinstance(cell, CandidateCell) or possible_value not in cell.get_possible_values():\
                            continue

                        # print(f"Need remove {possible_value} in R{row_order}C{row_coordinate.get_order()}")

                        exclude_cell_coordinates.add((
                            TwoDimensionalCoordinate(row_coordinate.get_order(), row_order),
                            possible_value,
                        ))
            # print(f"Number {possible_value}, there are {len(possible_columns)} possible columns")

        # print("============")
        for exclude_cell_coordinate, exclude_value in exclude_cell_coordinates:
            field.set_cell(exclude_cell_coordinate, field.get_cell(exclude_cell_coordinate) - CandidateCell([exclude_value]))

        return field, len(exclude_cell_coordinates) > 0
