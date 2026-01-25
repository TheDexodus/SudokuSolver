from abc import ABC, abstractmethod


class Coordinate(ABC):
    @abstractmethod
    def get_id(self) -> str:
        pass

    @abstractmethod
    def __eq__(self, other: "Coordinate") -> bool:
        pass

    @abstractmethod
    def __hash__(self) -> int:
        pass

    @classmethod
    @abstractmethod
    def from_id(cls, id: str) -> "Coordinate":
        pass