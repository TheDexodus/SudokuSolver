import pytest

from src.cell.cell import Cell
from src.cell.constant_cell import ConstantCell
from src.cell.empty_cell import EmptyCell
from src.coordinate.two_dimensional_coordinate import TwoDimensionalCoordinate
from src.repository.grid_cell_repository import GridCellRepository


def test_size():
    repository = GridCellRepository((3, 3))

    assert repository.get_size() == (3, 3)
    assert repository.get_count_cells() == 9

def test_get_cell():
    repository = GridCellRepository((3, 3))

    assert isinstance(repository.get_cell(TwoDimensionalCoordinate(1, 1)), EmptyCell)

def test_set_cell():
    repository = GridCellRepository((3, 3))
    repository.set_cell(TwoDimensionalCoordinate(1, 1), ConstantCell(4))

    assert repository.get_cell(TwoDimensionalCoordinate(1, 1)) == ConstantCell(4)

def test_iterator():
    repository = GridCellRepository((3, 3))
    x, y = 1, 1

    for coordinate, cell in repository:
        assert isinstance(coordinate, TwoDimensionalCoordinate)
        assert isinstance(cell, Cell)
        assert coordinate == TwoDimensionalCoordinate(x, y)

        x = (x % 3) + 1

        if x == 1:
            y += 1