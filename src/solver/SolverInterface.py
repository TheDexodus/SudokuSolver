from abc import ABC, abstractmethod

from src.field.FieldInterface import FieldInterface


class SolverInterface(ABC):
    @abstractmethod
    def solve(self, field: FieldInterface) -> FieldInterface:
        pass