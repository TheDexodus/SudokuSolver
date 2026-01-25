from abc import ABC, abstractmethod

from src.field.field import Field

'''
    When we use some strategy, we will get new field and status about strategy work(success or nothing found)
'''
class Strategy(ABC):
    @abstractmethod
    def apply(self, field: Field) -> [Field, bool]:
        pass