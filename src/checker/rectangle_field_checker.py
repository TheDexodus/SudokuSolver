from src.checker.checker import Checker
from src.checker.grid_checker import GridChecker
from src.checker.line_checker import LineChecker
from src.field.line_builder import LineBuilder
from src.field.rectangle_field import RectangleField


class RectangleFieldChecker(Checker[RectangleField]):
    _line_checker: LineChecker
    _grid_checker: GridChecker

    def __init__(self, line_checker: LineChecker | None = None, grid_checker: GridChecker | None = None):
        if line_checker is None:
            line_checker = LineChecker()

        if grid_checker is None:
            grid_checker = GridChecker()

        self._line_checker = line_checker
        self._grid_checker = grid_checker

    def check_correct(self, obj: RectangleField) -> bool:
        lines = LineBuilder.build_all_vertical_lines(obj) + LineBuilder.build_all_horizontal_lines(obj)

        for line in lines:
            if not self._line_checker.check_correct(line):
                return False

        for coordinate, grid in obj:
            if not self._grid_checker.check_correct(grid):
                return False

        return True

    def check_final(self, obj: RectangleField) -> bool:
        lines = LineBuilder.build_all_vertical_lines(obj) + LineBuilder.build_all_horizontal_lines(obj)

        for line in lines:
            if not self._line_checker.check_final(line):
                return False

        for coordinate, grid in obj:
            if not self._grid_checker.check_final(grid):
                return False

        return True

    def support(self, obj: any) -> bool:
        return isinstance(obj, RectangleField)