from abc import ABC, abstractmethod

from src.field.field import Field


class Solver(ABC):
    @abstractmethod
    def solve(self, field: Field) -> Field:
        pass