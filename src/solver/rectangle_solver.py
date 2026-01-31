from src.checker.general_checker import GeneralChecker
from src.checker.rectangle_field_checker import RectangleFieldChecker
from src.field.rectangle_field import RectangleField
from src.solver.randomer.order_randomer import OrderRandomer
from src.solver.randomer.randomer import Randomer
from src.solver.solver import Solver
from src.solver.strategy.candidate_elimination_in_grid_strategy import CandidateEliminationInGridStrategy
from src.solver.strategy.hidden_single_strategy import HiddenSingleStrategy
from src.solver.strategy.init_candidates_strategy import InitialCandidatesStrategy
from src.solver.strategy.strategy import Strategy


class RectangleSolver(Solver):
    _strategies: list[Strategy]
    _general_checker: GeneralChecker
    _randomer: Randomer

    def __init__(self):
        self._strategies = [
            InitialCandidatesStrategy(),
            CandidateEliminationInGridStrategy(),
            HiddenSingleStrategy(),
        ]
        self._general_checker = GeneralChecker([
            RectangleFieldChecker(),
        ])
        self._randomer = OrderRandomer()

    def solve(self, field: RectangleField) -> RectangleField:
        self._randomer.reset()
        has_updates_in_loop = True
        loops_counter = 0
        limit = 1000

        while not self._general_checker.check_final(field) and limit > 0:
            limit -= 1

            if not has_updates_in_loop:
                if self._general_checker.check_correct(field):
                    field = self._randomer.next(field)
                else:
                    field = self._randomer.next()

                has_updates_in_loop = True

                if field is None:
                    raise RuntimeError("Sudoku can't resolve")

            while has_updates_in_loop:
                has_updates_in_loop = False
                loops_counter += 1

                for strategy in self._strategies:
                    field, has_updates = strategy.apply(field.clone())
                    has_updates_in_loop = has_updates_in_loop or has_updates

                    if has_updates:
                        break

        return field