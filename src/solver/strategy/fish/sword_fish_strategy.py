from src.field.rectangle_field import RectangleField
from src.solver.strategy.fish.abstract_fish_strategy import AbstractFishStrategy


class SwordFishStrategy(AbstractFishStrategy):
    def apply(self, field: RectangleField) -> tuple[RectangleField, bool]:
        return self._apply_fish_strategy(field, 3)