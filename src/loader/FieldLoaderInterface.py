from abc import ABC, abstractmethod

from src.field.FieldInterface import FieldInterface


class FieldLoaderInterface(ABC):
    @abstractmethod
    def load(self) -> FieldInterface:
        pass
