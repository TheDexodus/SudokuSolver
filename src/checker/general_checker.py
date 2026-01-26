from src.checker.checker import Checker


class GeneralChecker(Checker):
    _checkers: list[Checker]

    def __init__(self, checkers: list[Checker]):
        self._checkers = checkers

    def check_correct(self, obj: any) -> bool:
        for checker in self._checkers:
            if checker.support(obj):
                return checker.check_correct(obj)

        raise Exception("No checker found")

    def check_final(self, obj: any) -> bool:
        for checker in self._checkers:
            if checker.support(obj):
                return checker.check_final(obj)

        raise Exception("No checker found")

    def support(self, obj: any) -> bool:
        for checker in self._checkers:
            if checker.support(obj):
                return True

        return False

    def get_checkers(self) -> list[Checker]:
        return self._checkers