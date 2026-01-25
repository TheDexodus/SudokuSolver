from src.coordinate.coordinate import Coordinate


class AbstractCoordinate(Coordinate):
    def __eq__(self, other: Coordinate) -> bool:
        return self.get_id() == other.get_id()

    def __hash__(self):
        return hash(self.get_id())