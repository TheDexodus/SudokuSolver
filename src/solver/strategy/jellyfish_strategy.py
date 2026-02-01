from src.cell.candidate_cell import CandidateCell
from src.coordinate.two_dimensional_coordinate import TwoDimensionalCoordinate
from src.field.line_builder import LineBuilder
from src.field.rectangle_field import RectangleField
from src.repository.helper.candidate_helper import CandidateHelper
from src.solver.strategy.strategy import Strategy


class JellyfishStrategy(Strategy):
    """
        **Стратегия**: "Jellyfish"

        **Идея**:
        Если для некоторого числа N:
        – в четырёх разных строках оно может находиться
          только в четырёх одних и тех же колонках,
        то образуется структура Jellyfish.

        Аналогично:
        – в четырёх разных колонках число N может находиться
          только в четырёх одних и тех же строках.

        **Следствие**:
        Число N исключается из всех остальных ячеек
        этих колонок (или строк соответственно).
    """

    def apply(self, field: RectangleField) -> tuple[RectangleField, bool]:
        exclude_cell_coordinates = set()

        # === Jellyfish по строкам ===
        for base_row_order, base_row in enumerate(LineBuilder.build_all_row_lines(field), 1):
            possible_values = CandidateHelper.find_unique_possible_values(base_row)

            for value in possible_values:
                base_candidates = CandidateHelper.find_candidate_cells_with_possible_value(base_row, value)
                if not (2 <= len(base_candidates) <= 4):
                    continue

                base_columns = {coord.get_order() for coord, _ in base_candidates}
                rows_with_same_columns = {base_row_order}

                for row_order, row_line in enumerate(LineBuilder.build_all_row_lines(field), 1):
                    if row_order == base_row_order:
                        continue

                    candidates = CandidateHelper.find_candidate_cells_with_possible_value(row_line, value)
                    if not (2 <= len(candidates) <= 4):
                        continue

                    columns = {coord.get_order() for coord, _ in candidates}
                    if columns.issubset(base_columns):
                        rows_with_same_columns.add(row_order)

                if len(rows_with_same_columns) != 4:
                    continue

                for column_order in base_columns:
                    column_line = LineBuilder.build_column_line(field, column_order)
                    for row_coord, cell in column_line:
                        if row_coord.get_order() in rows_with_same_columns:
                            continue

                        if isinstance(cell, CandidateCell) and value in cell.get_possible_values():
                            exclude_cell_coordinates.add(
                                (TwoDimensionalCoordinate(column_order, row_coord.get_order()), value)
                            )

        # === Jellyfish по колонкам ===
        for base_column_order, base_column in enumerate(LineBuilder.build_all_column_lines(field), 1):
            possible_values = CandidateHelper.find_unique_possible_values(base_column)

            for value in possible_values:
                base_candidates = CandidateHelper.find_candidate_cells_with_possible_value(base_column, value)
                if not (2 <= len(base_candidates) <= 4):
                    continue

                base_rows = {coord.get_order() for coord, _ in base_candidates}
                columns_with_same_rows = {base_column_order}

                for column_order, column_line in enumerate(LineBuilder.build_all_column_lines(field), 1):
                    if column_order == base_column_order:
                        continue

                    candidates = CandidateHelper.find_candidate_cells_with_possible_value(column_line, value)
                    if not (2 <= len(candidates) <= 4):
                        continue

                    rows = {coord.get_order() for coord, _ in candidates}
                    if rows.issubset(base_rows):
                        columns_with_same_rows.add(column_order)

                if len(columns_with_same_rows) != 4:
                    continue

                for row_order in base_rows:
                    row_line = LineBuilder.build_row_line(field, row_order)
                    for col_coord, cell in row_line:
                        if col_coord.get_order() in columns_with_same_rows:
                            continue

                        if isinstance(cell, CandidateCell) and value in cell.get_possible_values():
                            exclude_cell_coordinates.add(
                                (TwoDimensionalCoordinate(col_coord.get_order(), row_order), value)
                            )

        for coordinate, value in exclude_cell_coordinates:
            field.set_cell(
                coordinate,
                field.get_cell(coordinate) - CandidateCell([value])
            )

        return field, len(exclude_cell_coordinates) > 0
