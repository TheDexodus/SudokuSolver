from src.repository.CellRepositoryInterface import CellRepositoryInterface
from src.cell.CandidateCell import CandidateCell


class PossibleHelper:
    @classmethod
    def get_possible_cell(cls, line: CellRepositoryInterface) -> CandidateCell:
        values = set()
        possible_cell = CandidateCell()

        for cell in line.get_cells():
            if cell is not None and cell.get_value() is not None:
                values.add(cell.get_value())

        for i in range(1, line.get_max_count_cells() + 1):
            if i not in values:
                possible_cell.add_possible_value(i)

        return possible_cell