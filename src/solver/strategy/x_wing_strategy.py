from cv2.gapi.wip.draw import Line

from src.cell.candidate_cell import CandidateCell
from src.coordinate.two_dimensional_coordinate import TwoDimensionalCoordinate
from src.field.field import Field
from src.field.line_builder import LineBuilder
from src.field.rectangle_field import RectangleField
from src.repository.helper.candidate_helper import CandidateHelper
from src.solver.strategy.strategy import Strategy


class XWingStrategy(Strategy):
    """
        **Стратегия**: "X-Wing"

        **Идея**:
        Если для некоторого числа N:
        – в двух разных строках оно может находиться
          ровно в двух одних и тех же колонках,
        то эти четыре ячейки образуют структуру X-Wing.

        Аналогично:
        – в двух разных колонках число N может находиться
          ровно в двух одних и тех же строках.

        **Следствие**:
        Число N не может находиться ни в одной другой ячейке
        этих колонок (или строк соответственно) и может быть
        исключено из всех остальных ячеек.
    """

    def apply(self, field: RectangleField) -> tuple[RectangleField, bool]:
        exclude_cell_coordinates = set()

        for row_order, row_line in enumerate(LineBuilder.build_all_row_lines(field), 1):
            possible_values_in_line = CandidateHelper.find_unique_possible_values(row_line)

            for possible_value in possible_values_in_line:
                if CandidateHelper.count_candidate_cells_with_possible_value(row_line, possible_value) != 2:
                    continue

                candidate_cells = CandidateHelper.find_candidate_cells_with_possible_value(row_line, possible_value)
                candidates_by_row = {}

                for column_coordinate, candidate_cell in candidate_cells:
                    column_line = LineBuilder.build_column_line(field, column_coordinate.get_order())

                    if CandidateHelper.count_candidate_cells_with_possible_value(column_line, possible_value) < 2:
                        break

                    candidates_in_column = CandidateHelper.find_candidate_cells_with_possible_value(column_line, possible_value)

                    for row_coordinate, candidate_in_column in candidates_in_column:
                        if row_coordinate.get_order() == row_order:
                            continue

                        if CandidateHelper.count_candidate_cells_with_possible_value(LineBuilder.build_row_line(field, row_coordinate.get_order()), possible_value) != 2:
                            continue

                        candidates_by_row[row_coordinate.get_order()] = 1 if row_coordinate.get_order() not in candidates_by_row else (candidates_by_row[row_coordinate.get_order()] + 1)

                for candidate_row_order, count_candidates in candidates_by_row.items():
                    if count_candidates < 2:
                        continue

                    exclude_column_lines = [
                        (candidate_cells[0][0].get_order(), LineBuilder.build_column_line(field, candidate_cells[0][0].get_order())),
                        (candidate_cells[1][0].get_order(), LineBuilder.build_column_line(field, candidate_cells[1][0].get_order())),
                    ]

                    for exclude_column_order, exclude_column_line in exclude_column_lines:
                        for exclude_coordinate, exclude_cell in exclude_column_line:
                            if not isinstance(exclude_cell, CandidateCell):
                                continue

                            if possible_value not in exclude_cell.get_possible_values():
                                continue

                            if exclude_coordinate.get_order() == row_order or exclude_coordinate.get_order() == candidate_row_order:
                                continue

                            exclude_cell_coordinates.add((TwoDimensionalCoordinate(exclude_column_order, exclude_coordinate.get_order()), possible_value))

        for column_order, column_line in enumerate(LineBuilder.build_all_column_lines(field), 1):
            possible_values_in_line = CandidateHelper.find_unique_possible_values(column_line)

            for possible_value in possible_values_in_line:
                if CandidateHelper.count_candidate_cells_with_possible_value(column_line, possible_value) != 2:
                    continue

                candidate_cells = CandidateHelper.find_candidate_cells_with_possible_value(column_line, possible_value)
                candidates_by_column = {}

                for row_coordinate, candidate_cell in candidate_cells:
                    row_line = LineBuilder.build_row_line(field, row_coordinate.get_order())

                    if CandidateHelper.count_candidate_cells_with_possible_value(row_line, possible_value) < 2:
                        break

                    candidates_in_row = CandidateHelper.find_candidate_cells_with_possible_value(row_line, possible_value)

                    for column_coordinate, candidate_in_row in candidates_in_row:
                        if column_coordinate.get_order() == column_order:
                            continue

                        if CandidateHelper.count_candidate_cells_with_possible_value(LineBuilder.build_column_line(field, column_coordinate.get_order()), possible_value) != 2:
                            continue

                        candidates_by_column[column_coordinate.get_order()] = 1 if column_coordinate.get_order() not in candidates_by_column else (candidates_by_column[column_coordinate.get_order()] + 1)

                for candidate_column_order, count_candidates in candidates_by_column.items():
                    if count_candidates < 2:
                        continue

                    exclude_row_lines = [
                        (candidate_cells[0][0].get_order(), LineBuilder.build_row_line(field, candidate_cells[0][0].get_order())),
                        (candidate_cells[1][0].get_order(), LineBuilder.build_row_line(field, candidate_cells[1][0].get_order())),
                    ]

                    for exclude_row_order, exclude_row_line in exclude_row_lines:
                        for exclude_coordinate, exclude_cell in exclude_row_line:
                            if not isinstance(exclude_cell, CandidateCell):
                                continue

                            if possible_value not in exclude_cell.get_possible_values():
                                continue

                            if exclude_coordinate.get_order() == column_order or exclude_coordinate.get_order() == candidate_column_order:
                                continue

                            exclude_cell_coordinates.add((TwoDimensionalCoordinate(exclude_coordinate.get_order(), exclude_row_order), possible_value))

        for exclude_cell_coordinate, exclude_value in exclude_cell_coordinates:
            field.set_cell(exclude_cell_coordinate, field.get_cell(exclude_cell_coordinate) - CandidateCell([exclude_value]))

        return field, len(exclude_cell_coordinates) > 0