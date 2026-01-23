from abc import ABC, abstractmethod


class CoordinateInterface(ABC):
    @abstractmethod
    def get_id(self) -> str:
        pass

    @abstractmethod
    def __eq__(self, other: "CoordinateInterface") -> bool:
        pass

    @abstractmethod
    def __hash__(self) -> int:
        pass

    @classmethod
    @abstractmethod
    def from_id(cls, id: str) -> "CoordinateInterface":
        pass