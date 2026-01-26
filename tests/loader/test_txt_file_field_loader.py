import pytest

import os

from src.field.rectangle_field import RectangleField
from src.loader.txt_file_field_loader import TxtFileFieldLoader

TESTDATA_FILENAME = os.path.join(os.path.dirname(__file__), '../data/sudoku/sudoku.txt')


def test_load():
    loader = TxtFileFieldLoader(TESTDATA_FILENAME)
    field = loader.load()

    assert isinstance(field, RectangleField)
    assert str(field).strip() == '''
+-------+-------+-------+
|   2 3 | 4 5 6 | 7 8 9 |
| 1   3 | 4 5 6 | 7 8 9 |
| 1 2   | 4 5 6 | 7 8 9 |
+-------+-------+-------+
| 1 2 3 |   5 6 | 7 8 9 |
| 1 2 3 | 4   6 | 7 8 9 |
| 1 2 3 | 4 5   | 7 8 9 |
+-------+-------+-------+
| 1 2 3 | 4 5 6 |   8 9 |
| 1 2 3 | 4 5 6 | 7   9 |
| 1 2 3 | 4 5 6 | 7 8   |
+-------+-------+-------+
        '''.strip()