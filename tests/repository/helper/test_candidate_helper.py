from src.cell.candidate_cell import CandidateCell
from src.cell.constant_cell import ConstantCell
from src.coordinate.ordinal_coordinate import OrdinalCoordinate
from src.repository.helper.candidate_helper import CandidateHelper
from src.repository.line_cell_repository import LineCellRepository


def test_find_unique_possible_values():
    repository = LineCellRepository(9)
    repository.set_cell(OrdinalCoordinate(1), ConstantCell(1))
    repository.set_cell(OrdinalCoordinate(2), ConstantCell(2))
    repository.set_cell(OrdinalCoordinate(3), CandidateCell([3, 4, 5]))
    repository.set_cell(OrdinalCoordinate(4), CandidateCell([5, 6, 7]))
    repository.set_cell(OrdinalCoordinate(5), CandidateCell([6, 7, 8]))
    repository.set_cell(OrdinalCoordinate(6), CandidateCell([3, 8]))
    repository.set_cell(OrdinalCoordinate(7), CandidateCell([4, 5]))
    repository.set_cell(OrdinalCoordinate(8), CandidateCell([3, 6]))
    repository.set_cell(OrdinalCoordinate(9), ConstantCell(9))

    assert CandidateHelper.find_unique_possible_values(repository) == [3, 4, 5, 6, 7, 8]

def test_count_candidate_cells_with_possible_value():
    repository = LineCellRepository(9)
    repository.set_cell(OrdinalCoordinate(1), ConstantCell(1))
    repository.set_cell(OrdinalCoordinate(2), ConstantCell(2))
    repository.set_cell(OrdinalCoordinate(3), CandidateCell([3, 4, 5]))
    repository.set_cell(OrdinalCoordinate(4), CandidateCell([5, 6, 7]))
    repository.set_cell(OrdinalCoordinate(5), CandidateCell([6, 7, 8]))
    repository.set_cell(OrdinalCoordinate(6), CandidateCell([3, 8]))
    repository.set_cell(OrdinalCoordinate(7), CandidateCell([4, 5]))
    repository.set_cell(OrdinalCoordinate(8), CandidateCell([3, 6]))
    repository.set_cell(OrdinalCoordinate(9), ConstantCell(9))

    assert CandidateHelper.count_candidate_cells_with_possible_value(repository, 3) == 3
    assert CandidateHelper.count_candidate_cells_with_possible_value(repository, 4) == 2
    assert CandidateHelper.count_candidate_cells_with_possible_value(repository, 5) == 3
    assert CandidateHelper.count_candidate_cells_with_possible_value(repository, 6) == 3
    assert CandidateHelper.count_candidate_cells_with_possible_value(repository, 7) == 2
    assert CandidateHelper.count_candidate_cells_with_possible_value(repository, 8) == 2