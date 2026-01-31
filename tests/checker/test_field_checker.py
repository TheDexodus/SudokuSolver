import pytest

from src.checker.rectangle_field_checker import RectangleFieldChecker
from src.field.rectangle_field import RectangleField
from tests.data.sudoku.cases import load_final_cases, load_correct_not_final_cases, load_incorrect_cases


@pytest.mark.parametrize(
    "field",
    load_final_cases()
)
def test_load_final(field: RectangleField):
    field_checker = RectangleFieldChecker()

    assert field_checker.check_correct(field)
    assert field_checker.check_final(field)


@pytest.mark.parametrize(
    "field",
    load_correct_not_final_cases()
)
def test_load_correct_not_final(field: RectangleField):
    field_checker = RectangleFieldChecker()

    assert field_checker.check_correct(field)
    assert not field_checker.check_final(field)

@pytest.mark.parametrize(
    "field",
    load_incorrect_cases()
)
def test_load_incorrect(field: RectangleField):
    field_checker = RectangleFieldChecker()

    assert not field_checker.check_correct(field)
    assert not field_checker.check_final(field)