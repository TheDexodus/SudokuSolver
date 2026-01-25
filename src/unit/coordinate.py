from typing import Iterator


class Coordinate:
    x: int
    y: int

    def __init__(self, x: int, y: int) -> None:
        self.x = x
        self.y = y

    @classmethod
    def from_tuple(cls, pair: tuple[int, int]) -> "Coordinate":
        return cls(pair[0], pair[1])

    def in_bounds(self, start_bound: "Coordinate", end_bound: "Coordinate") -> bool:
        return start_bound.x <= self.x <= end_bound.x and start_bound.y <= self.y <= end_bound.y

    def to_tuple(self) -> tuple[int, int]:
        return self.x, self.y

    def __iter__(self) -> Iterator["Coordinate"]:
        return iter(self.to_tuple())

    def __str__(self) -> str:
        return f"({self.x}, {self.y})"

    def __repr__(self) -> str:
        return str(self)