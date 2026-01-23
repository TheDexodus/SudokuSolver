from src.coordinate.CoordinateInterface import CoordinateInterface


class AbstractCoordinate(CoordinateInterface):
    def __eq__(self, other: CoordinateInterface) -> bool:
        return self.get_id() == other.get_id()

    def __hash__(self):
        return hash(self.get_id())