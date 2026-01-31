from abc import ABC, abstractmethod

from src.field.field import Field


class Randomer(ABC):
    @abstractmethod
    def reset(self):
        pass

    @abstractmethod
    def next(self, new_field: Field|None = None) -> Field|None:
        pass