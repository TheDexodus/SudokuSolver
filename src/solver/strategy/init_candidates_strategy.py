from src.field.field import Field
from src.solver.solver import Solver


class InitialCandidatesStrategy(Solver):
    def solve(self, field: Field) -> [Field, bool]:
