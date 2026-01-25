from abc import ABC, abstractmethod

from src.field.field import Field


class FieldLoader(ABC):
    @abstractmethod
    def load(self) -> Field:
        pass
