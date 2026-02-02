from src.cell.candidate_cell import CandidateCell
from src.cell.constant_cell import ConstantCell
from src.coordinate.two_dimensional_coordinate import TwoDimensionalCoordinate
from src.field.rectangle_field import RectangleField
from src.solver.strategy.hidden.hidden_single_strategy import HiddenSingleStrategy


def make_field_for_test_grid() -> RectangleField:
    field = RectangleField((3, 3))
    first_grid = field.get_grid(TwoDimensionalCoordinate(1, 1))

    first_grid.set_cell(TwoDimensionalCoordinate(1, 1), CandidateCell([1, 2]))
    first_grid.set_cell(TwoDimensionalCoordinate(1, 2), CandidateCell([2, 3]))
    first_grid.set_cell(TwoDimensionalCoordinate(1, 3), CandidateCell([2, 3]))
    first_grid.set_cell(TwoDimensionalCoordinate(2, 1), CandidateCell([2, 3]))
    first_grid.set_cell(TwoDimensionalCoordinate(2, 2), CandidateCell([2, 3]))
    first_grid.set_cell(TwoDimensionalCoordinate(2, 3), CandidateCell([2, 3]))
    first_grid.set_cell(TwoDimensionalCoordinate(3, 1), CandidateCell([2, 3]))
    first_grid.set_cell(TwoDimensionalCoordinate(3, 2), CandidateCell([2, 3]))
    first_grid.set_cell(TwoDimensionalCoordinate(3, 3), CandidateCell([2, 3]))

    return field

def make_field_for_test_horizontal_line() -> RectangleField:
    field = RectangleField((3, 3))
    first_grid = field.get_grid(TwoDimensionalCoordinate(1, 3))
    second_grid = field.get_grid(TwoDimensionalCoordinate(2, 3))
    third_grid = field.get_grid(TwoDimensionalCoordinate(3, 3))

    first_grid.set_cell(TwoDimensionalCoordinate(1, 2), CandidateCell([2, 5, 6]))
    first_grid.set_cell(TwoDimensionalCoordinate(2, 2), ConstantCell(9))
    first_grid.set_cell(TwoDimensionalCoordinate(3, 2), ConstantCell(3))

    second_grid.set_cell(TwoDimensionalCoordinate(1, 2), CandidateCell([2, 5, 7]))
    second_grid.set_cell(TwoDimensionalCoordinate(2, 2), CandidateCell([3, 6, 7, 8, 9]))
    second_grid.set_cell(TwoDimensionalCoordinate(3, 2), CandidateCell([2, 4, 5, 6, 8, 9]))

    third_grid.set_cell(TwoDimensionalCoordinate(1, 2), ConstantCell(7))
    third_grid.set_cell(TwoDimensionalCoordinate(2, 2), CandidateCell([1, 3]))
    third_grid.set_cell(TwoDimensionalCoordinate(3, 2), CandidateCell([4, 5, 8]))

    first_grid.set_cell(TwoDimensionalCoordinate(1, 1), CandidateCell([2, 4, 5, 6, 7, 8]))
    first_grid.set_cell(TwoDimensionalCoordinate(2, 1), CandidateCell([2, 4, 5, 6, 7, 8]))
    first_grid.set_cell(TwoDimensionalCoordinate(3, 1), CandidateCell([2, 4, 5, 6, 7, 8]))

    second_grid.set_cell(TwoDimensionalCoordinate(1, 1), CandidateCell([2, 3, 4, 5, 6, 7, 8 ,9]))
    second_grid.set_cell(TwoDimensionalCoordinate(2, 1), CandidateCell([2, 3, 4, 5, 6, 7, 8 ,9]))
    second_grid.set_cell(TwoDimensionalCoordinate(3, 1), CandidateCell([2, 3, 4, 5, 6, 7, 8 ,9]))

    third_grid.set_cell(TwoDimensionalCoordinate(1, 1), CandidateCell([1, 2, 3, 4, 5, 6, 8 ,9]))
    third_grid.set_cell(TwoDimensionalCoordinate(2, 1), CandidateCell([1, 2, 3, 4, 5, 6, 8 ,9]))
    third_grid.set_cell(TwoDimensionalCoordinate(3, 1), CandidateCell([1, 2, 3, 4, 5, 6, 8 ,9]))

    first_grid.set_cell(TwoDimensionalCoordinate(1, 3), CandidateCell([2, 4, 5, 6, 7, 8]))
    first_grid.set_cell(TwoDimensionalCoordinate(2, 3), CandidateCell([2, 4, 5, 6, 7, 8]))
    first_grid.set_cell(TwoDimensionalCoordinate(3, 3), CandidateCell([2, 4, 5, 6, 7, 8]))

    second_grid.set_cell(TwoDimensionalCoordinate(1, 3), CandidateCell([2, 3, 4, 5, 6, 7, 8 ,9]))
    second_grid.set_cell(TwoDimensionalCoordinate(2, 3), CandidateCell([2, 3, 4, 5, 6, 7, 8 ,9]))
    second_grid.set_cell(TwoDimensionalCoordinate(3, 3), CandidateCell([2, 3, 4, 5, 6, 7, 8 ,9]))

    third_grid.set_cell(TwoDimensionalCoordinate(1, 3), CandidateCell([1, 2, 3, 4, 5, 6, 8 ,9]))
    third_grid.set_cell(TwoDimensionalCoordinate(2, 3), CandidateCell([1, 2, 3, 4, 5, 6, 8 ,9]))
    third_grid.set_cell(TwoDimensionalCoordinate(3, 3), CandidateCell([1, 2, 3, 4, 5, 6, 8 ,9]))

    return field

def make_field_for_test_vertical_line() -> RectangleField:
    field = RectangleField((3, 3))
    first_grid = field.get_grid(TwoDimensionalCoordinate(1, 1))
    second_grid = field.get_grid(TwoDimensionalCoordinate(1, 2))
    third_grid = field.get_grid(TwoDimensionalCoordinate(1, 3))

    first_grid.set_cell(TwoDimensionalCoordinate(1, 1), CandidateCell([1, 2]))
    first_grid.set_cell(TwoDimensionalCoordinate(1, 2), CandidateCell([1, 2]))
    first_grid.set_cell(TwoDimensionalCoordinate(1, 3), CandidateCell([1, 2]))

    second_grid.set_cell(TwoDimensionalCoordinate(1, 1), CandidateCell([1, 2]))
    second_grid.set_cell(TwoDimensionalCoordinate(1, 2), CandidateCell([1, 2, 3]))
    second_grid.set_cell(TwoDimensionalCoordinate(1, 3), CandidateCell([1, 2]))

    third_grid.set_cell(TwoDimensionalCoordinate(1, 1), CandidateCell([1, 2]))
    third_grid.set_cell(TwoDimensionalCoordinate(1, 2), CandidateCell([1, 2]))
    third_grid.set_cell(TwoDimensionalCoordinate(1, 3), CandidateCell([1, 2]))

    second_grid.set_cell(TwoDimensionalCoordinate(2, 2), CandidateCell([1, 2, 3]))

    return field

def test_hidden_single_strategy_for_grid():
    strategy = HiddenSingleStrategy()
    field, has_updates = strategy.apply(make_field_for_test_grid())

    assert has_updates == True

    first_cell = field.get_grid(TwoDimensionalCoordinate(1, 1)).get_cell(TwoDimensionalCoordinate(1, 1))
    assert isinstance(first_cell, ConstantCell)
    assert first_cell.value == 1

def test_hidden_single_strategy_for_horizontal_line():
    strategy = HiddenSingleStrategy()
    field, has_updates = strategy.apply(make_field_for_test_horizontal_line())

    assert has_updates == True

    cell = field.get_grid(TwoDimensionalCoordinate(3, 3)).get_cell(TwoDimensionalCoordinate(2, 2))

    assert isinstance(cell, ConstantCell)
    assert cell.value == 1

def test_hidden_single_strategy_for_vertical_line():
    strategy = HiddenSingleStrategy()
    field, has_updates = strategy.apply(make_field_for_test_vertical_line())
    assert has_updates == True

    cell = field.get_grid(TwoDimensionalCoordinate(1, 2)).get_cell(TwoDimensionalCoordinate(1, 2))

    assert isinstance(cell, ConstantCell)
    assert cell.value == 3