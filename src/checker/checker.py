from abc import ABC, abstractmethod
from typing import TypeVar, Generic

TCheckObject = TypeVar('TCheckObject')

class Checker(ABC, Generic[TCheckObject]):
    @abstractmethod
    def check_correct(self, obj: TCheckObject) -> bool:
        pass

    @abstractmethod
    def check_final(self, obj: TCheckObject) -> bool:
        pass

    @abstractmethod
    def support(self, obj: any) -> bool:
        pass