from src.checker.checker import Checker
from src.repository.line_cell_repository import LineCellRepository


class LineChecker(Checker[LineCellRepository]):
    def check_correct(self, obj: LineCellRepository) -> bool:
        occurring_numbers = []

        for coordinate, cell in obj:
            if cell.get_value() is None:
                continue

            if cell.get_value() in occurring_numbers:
                return False

            occurring_numbers.append(cell.get_value())

        return True

    def check_final(self, obj: LineCellRepository) -> bool:
        if not self.check_correct(obj):
            return False

        for coordinate, cell in obj:
            if cell.get_value() is None:
                return False

        return True

    def support(self, obj: any) -> bool:
        return isinstance(obj, LineCellRepository)