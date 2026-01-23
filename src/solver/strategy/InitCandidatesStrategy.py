from src.field.FieldInterface import FieldInterface
from src.solver.SolverInterface import SolverInterface


class InitialCandidatesStrategy(SolverInterface):
    def solve(self, field: FieldInterface) -> [FieldInterface, bool]:
