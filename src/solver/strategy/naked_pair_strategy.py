from src.cell.candidate_cell import CandidateCell
from src.coordinate.coordinate import Coordinate
from src.coordinate.ordinal_coordinate import OrdinalCoordinate
from src.coordinate.two_dimensional_coordinate import TwoDimensionalCoordinate
from src.field.line_builder import LineBuilder
from src.field.rectangle_field import RectangleField
from src.repository.cell_repository import CellRepository
from src.solver.strategy.strategy import Strategy


class NakedPairStrategy(Strategy):
    """
        **Стратегия**: "Голая пара" (Naked Pair)

        **Идея**:
        Если в рамках одного CellRepository (строка / колонка / grid)
        существуют ровно две ячейки, в которых возможны только одни и те же
        два значения, то эти два значения обязаны находиться именно в этих
        двух ячейках.

        **Следствие**:
        Эти значения можно исключить из всех остальных ячеек
        данного CellRepository.
    """

    def apply(self, field: RectangleField) -> tuple[RectangleField, bool]:
        has_updates = False

        # Поиск в рамках одного column
        for column_order, column_line in enumerate(LineBuilder.build_all_vertical_lines(field), 1):
            changes: list[tuple[OrdinalCoordinate, CandidateCell]] = self._apply_for_repository(column_line)

            for cell_coordinate, new_cell in changes:
                field.set_cell(TwoDimensionalCoordinate(column_order, cell_coordinate.get_order()), new_cell)

        # Поиск в рамках одного row
        for row_order, row_line in enumerate(LineBuilder.build_all_horizontal_lines(field), 1):
            changes: list[tuple[OrdinalCoordinate, CandidateCell]] = self._apply_for_repository(row_line)

            for cell_coordinate, new_cell in changes:
                field.set_cell(TwoDimensionalCoordinate(cell_coordinate.get_order(), row_order), new_cell)

        # Поиск в рамках одного grid
        for grid_coordinate, grid in field:
            changes: list[tuple[TwoDimensionalCoordinate, CandidateCell]] = self._apply_for_repository(grid)

            for cell_coordinate, new_cell in changes:
                grid.set_cell(cell_coordinate, new_cell)

        return field, has_updates

    def _apply_for_repository(self, repository: CellRepository) -> list[tuple[Coordinate, CandidateCell]]:
        changes: list[tuple[Coordinate, CandidateCell]] = []

        for cell_coordinate, cell in repository:
            # Если это не кандидат или кандидат с не двумя возможными значениями - скипаем
            if not isinstance(cell, CandidateCell) or len(cell.get_possible_values()) != 2:
                continue

            # Ищем второго кандидата с таким же набором возможных значений
            for second_cell_coordinate, second_cell in repository:
                if second_cell_coordinate == cell_coordinate:
                    continue

                if cell == second_cell:
                    # Ищем кандидата в котором указывались возможные значения из голой пары чтобы исключить
                    for third_cell_coordinate, third_cell in repository:
                        if not isinstance(third_cell, CandidateCell):
                            continue

                        if third_cell_coordinate == cell_coordinate or third_cell_coordinate == second_cell_coordinate:
                            continue

                        for possible_value in third_cell.get_possible_values():
                            if possible_value not in cell.get_possible_values():
                                continue

                            changes.append((third_cell_coordinate, third_cell - cell))
                            break

        return changes