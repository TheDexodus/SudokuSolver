from src.coordinate.abstract_coordinate import AbstractCoordinate


class OrdinalCoordinate(AbstractCoordinate):
    def __init__(self, order: int):
        self._order = order

    def get_id(self) -> str:
        return f"{self._order}"

    def get_order(self) -> int:
        return self._order

    @classmethod
    def from_id(cls, id: str) -> "OrdinalCoordinate":
        return OrdinalCoordinate(int(id))