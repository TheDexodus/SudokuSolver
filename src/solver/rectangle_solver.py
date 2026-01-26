from src.checker.general_checker import GeneralChecker
from src.checker.rectangle_field_checker import RectangleFieldChecker
from src.field.field import Field
from src.solver.solver import Solver
from src.solver.strategy.candidate_elimination_in_grid_strategy import CandidateEliminationInGridStrategy
from src.solver.strategy.init_candidates_strategy import InitialCandidatesStrategy
from src.solver.strategy.strategy import Strategy


class RectangleSolver(Solver):
    _strategies: list[Strategy]
    _general_checker: GeneralChecker

    def __init__(self):
        self._strategies = [
            InitialCandidatesStrategy(),
            CandidateEliminationInGridStrategy(),
        ]
        self._general_checker = GeneralChecker([
            RectangleFieldChecker(),
        ])

    def solve(self, field: Field) -> Field:
        limit = 1000

        while not self._general_checker.check_final(field) and limit > 0:
            for strategy in self._strategies:
                field, has_updates = strategy.apply(field)

                if has_updates:
                    print("Has updates in strategy: ", strategy)
                    break

            limit -= 1

        return field