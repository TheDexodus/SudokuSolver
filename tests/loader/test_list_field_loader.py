import pytest

from src.field.rectangle_field import RectangleField
from src.loader.list_field_loader import ListFieldLoader


def test_load():
    loader = ListFieldLoader([
        [None, 2, 3, 4, 5, 6, 7, 8, 9],
        [1, 0, 3, 4, 5, 6, 7, 8, 9],
        [1, 2, None, 4, 5, 6, 7, 8, 9],
        [1, 2, 3, 0, 5, 6, 7, 8, 9],
        [1, 2, 3, 4, None, 6, 7, 8, 9],
        [1, 2, 3, 4, 5, 0, 7, 8, 9],
        [1, 2, 3, 4, 5, 6, None, 8, 9],
        [1, 2, 3, 4, 5, 6, 7, 0, 9],
        [1, 2, 3, 4, 5, 6, 7, 8, None],
    ])

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