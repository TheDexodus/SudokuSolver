from abc import ABC, abstractmethod

from src.field.FieldInterface import FieldInterface

'''
    When we use some strategy, we will get new field and status about strategy work(success or nothing found)
'''
class StrategyInterface(ABC):
    @abstractmethod
    def apply(self, field: FieldInterface) -> [FieldInterface, bool]:
        pass