from src.cell.candidate_cell import CandidateCell
from src.coordinate.coordinate import Coordinate
from src.repository.cell_repository import CellRepository


class CandidateHelper:
    @classmethod
    def find_unique_possible_values(cls, repository: CellRepository) -> list[int]:
        unique_possible_values = set()

        for _, cell in repository:
            if not isinstance(cell, CandidateCell):
                continue

            for possible_value in cell.get_possible_values():
                unique_possible_values.add(possible_value)

        return list(unique_possible_values)

    @classmethod
    def count_candidate_cells_with_possible_value(cls, repository: CellRepository, possible_value: int) -> int:
        count = 0

        for _, cell in repository:
            if not isinstance(cell, CandidateCell):
                continue

            if possible_value in cell.get_possible_values():
                count += 1

        return count

    @classmethod
    def find_candidate_cells_with_possible_value(cls, repository: CellRepository, possible_value: int) -> list[tuple[Coordinate, CandidateCell]]:
        candidate_cells = []

        for coordinate, cell in repository:
            if not isinstance(cell, CandidateCell):
                continue

            if possible_value in cell.get_possible_values():
                candidate_cells.append((coordinate, cell))

        return candidate_cells