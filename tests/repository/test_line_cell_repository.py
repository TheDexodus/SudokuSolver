import pytest

from src.coordinate.ordinal_coordinate import OrdinalCoordinate
from src.cell.constant_cell import ConstantCell
from src.cell.empty_cell import EmptyCell
from src.repository.line_cell_repository import LineCellRepository

def test_size():
    repository = LineCellRepository(9)

    assert repository.get_count_cells() == 9

def test_get_cells():
    repository = LineCellRepository(9)

    for index, (coordinate, cell) in enumerate(repository.get_cells().items(), 1):
        assert isinstance(coordinate, OrdinalCoordinate)
        assert isinstance(cell, EmptyCell)
        assert coordinate.get_order() == index

def test_set_and_get_cell():
    repository = LineCellRepository(9)
    repository.set_cell(OrdinalCoordinate(1), ConstantCell(5))
    assert repository.get_cell(OrdinalCoordinate(1)) == ConstantCell(5)

def test_iter():
    repository = LineCellRepository(9)

    for coordinate, cell in repository:
        assert isinstance(coordinate, OrdinalCoordinate)
        assert isinstance(cell, EmptyCell)