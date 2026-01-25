import pytest

from src.repository.grid_cell_repository import GridCellRepository


def test_size():
    repository = GridCellRepository((3, 3))

    assert repository.get_size() == (3, 3)
    assert repository.get_count_cells() == 9