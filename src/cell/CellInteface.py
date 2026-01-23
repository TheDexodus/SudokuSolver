from abc import ABC, abstractmethod


class CellInterface(ABC):
    @abstractmethod
    def get_value(self) -> int | None:
        pass

    @abstractmethod
    def can_be_replaced(self) -> bool:
        pass

    @abstractmethod
    def __str__(self):
        pass