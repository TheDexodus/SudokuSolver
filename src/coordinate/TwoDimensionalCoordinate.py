from src.coordinate.AbstractCoordinate import AbstractCoordinate


class TwoDimensionalCoordinate(AbstractCoordinate):
    def __init__(self, x: int, y: int) -> None:
        self._x = x
        self._y = y

    def get_id(self) -> str:
        return f"{self._x},{self._y}"

    def get_x(self) -> int:
        return self._x

    def get_y(self) -> int:
        return self._y

    @classmethod
    def from_id(cls, id: str) -> "TwoDimensionalCoordinate":
        x, y = id.split(",")
        return TwoDimensionalCoordinate(int(x), int(y))