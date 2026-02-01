from src.cell.candidate_cell import CandidateCell
from src.cell.constant_cell import ConstantCell
from src.field.rectangle_field import RectangleField
from src.solver.strategy.strategy import Strategy


class LastHeroStrategy(Strategy):
    """
        **Стратегия**: "Последний герой" (Naked Single)

        **Идея**:
        Если ячейка содержит ровно одно возможное значение (кандидат),
        то это значение обязательно должно быть установлено в данной ячейке.

        Такая ситуация возникает после исключения всех невозможных
        кандидатов другими стратегиями.

        **Следствие**:
        Ячейка с единственным возможным значением
        преобразуется из CandidateCell в ConstantCell.
    """

    def apply(self, field: RectangleField) -> tuple[RectangleField, bool]:
        has_updates = False

        for _, grid in field:
            for cell_coordinate, cell in grid:
                if not isinstance(cell, CandidateCell):
                    continue

                possible_values = cell.get_possible_values()
                if len(possible_values) != 1:
                    continue

                value = possible_values[0]
                grid.set_cell(cell_coordinate, ConstantCell(value))
                has_updates = True

        return field, has_updates