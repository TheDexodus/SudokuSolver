from src.cell.candidate_cell import CandidateCell
from src.cell.empty_cell import EmptyCell
from src.field.rectangle_field import RectangleField
from src.solver.strategy.strategy import Strategy


class InitialCandidatesStrategy(Strategy):
    """
        **Стратегия**: "Инициализация кандидатов" (Initial Candidates)

        **Идея**:
        Для каждой пустой ячейки игрового поля необходимо задать
        начальный набор возможных значений (кандидатов).

        На этом этапе не учитываются ограничения строк, колонок и grid —
        каждая пустая ячейка получает полный список допустимых значений
        для данного размера поля.

        **Следствие**:
        Все пустые ячейки переводятся в состояние CandidateCell
        с полным набором возможных значений.
        Дальнейшие стратегии работают уже с этим набором,
        постепенно исключая невозможные кандидаты.
    """

    def apply(self, field: RectangleField) -> tuple[RectangleField, bool]:
        have_updates = False

        for grid_coordinate, grid in field:
            for cell_coordinate, cell in grid:
                if isinstance(cell, EmptyCell):
                    have_updates = True
                    grid.set_cell(cell_coordinate, CandidateCell(self._get_possible_values(field)))

        return field, have_updates

    def _get_possible_values(self, field: RectangleField) -> list[int]:
        possible_values = []

        for possible_value in range(1, field.get_size()[0] * field.get_size()[1] + 1):
            possible_values.append(possible_value)

        return possible_values