from src.cell.candidate_cell import CandidateCell
from src.coordinate.coordinate import Coordinate
from src.coordinate.two_dimensional_coordinate import TwoDimensionalCoordinate
from src.field.line_builder import LineBuilder
from src.field.rectangle_field import RectangleField
from src.repository.cell_repository import CellRepository
from src.solver.strategy.strategy import Strategy


class NakedTripleStrategy(Strategy):
    """
        **Стратегия**: "Голая тройка" (Naked Triple)

        **Идея**:
        В рамках одного CellRepository (строка / колонка / grid)
        существуют ровно три ячейки, совокупность возможных значений
        которых состоит ровно из трёх чисел.

        При этом каждая из этих ячеек может содержать
        2 или 3 возможных значения, но их объединение
        образует ровно три значения.

        **Следствие**:
        Эти три значения обязаны находиться именно в этих
        трёх ячейках и могут быть исключены из всех остальных
        ячеек данного CellRepository.
    """

    def apply(self, field: RectangleField) -> tuple[RectangleField, bool]:
        has_updates = False

        # columns
        for column_order, column in enumerate(LineBuilder.build_all_column_lines(field), 1):
            changes = self._apply_for_repository(column)

            for cell_coordinate, new_cell in changes:
                field.set_cell(TwoDimensionalCoordinate(column_order, cell_coordinate.get_order()), new_cell)
                has_updates = True

        # rows
        for row_order, row in enumerate(LineBuilder.build_all_row_lines(field), 1):
            changes = self._apply_for_repository(row)

            for cell_coordinate, new_cell in changes:
                field.set_cell(TwoDimensionalCoordinate(cell_coordinate.get_order(), row_order), new_cell)
                has_updates = True

        # grids
        for _, grid in field:
            changes = self._apply_for_repository(grid)

            for cell_coordinate, new_cell in changes:
                grid.set_cell(cell_coordinate, new_cell)
                has_updates = True

        return field, has_updates

    def _apply_for_repository(self, repository: CellRepository) -> list[tuple[Coordinate, CandidateCell]]:
        changes: list[tuple[Coordinate, CandidateCell]] = []

        candidates: list[tuple[Coordinate, CandidateCell]] = [
            (coord, cell)
            for coord, cell in repository
            if isinstance(cell, CandidateCell) and 2 <= len(cell.get_possible_values()) <= 3
        ]

        # перебираем все комбинации троек
        for i in range(len(candidates)):
            for j in range(i + 1, len(candidates)):
                for k in range(j + 1, len(candidates)):
                    coords_cells = [candidates[i], candidates[j], candidates[k]]

                    union_values = set()
                    for _, cell in coords_cells:
                        union_values |= set(cell.get_possible_values())

                    # naked triple найден
                    if len(union_values) != 3:
                        continue

                    triple_coords = {coord for coord, _ in coords_cells}

                    for coord, cell in repository:
                        if not isinstance(cell, CandidateCell):
                            continue
                        if coord in triple_coords:
                            continue

                        new_cell = cell
                        for value in union_values:
                            if value in new_cell.get_possible_values():
                                new_cell = new_cell - value

                        if new_cell != cell:
                            changes.append((coord, new_cell))

        return changes