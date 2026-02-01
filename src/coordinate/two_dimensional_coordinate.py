from src.coordinate.abstract_coordinate import AbstractCoordinate


class TwoDimensionalCoordinate(AbstractCoordinate):
    def __init__(self, col: int, row: int) -> None:
        self._col = col
        self._row = row

    def get_id(self) -> str:
        return f"{self._col},{self._row}"

    def get_col(self) -> int:
        return self._col

    def get_row(self) -> int:
        return self._row

    @classmethod
    def from_id(cls, id: str) -> "TwoDimensionalCoordinate":
        col, row = id.split(",")
        return TwoDimensionalCoordinate(int(col), int(row))

    def __str__(self) -> str:
        return f"{self._col},{self._row}"

    def __repr__(self) -> str:
        return f"{self.__class__.__name__}({self._col},{self._row})"