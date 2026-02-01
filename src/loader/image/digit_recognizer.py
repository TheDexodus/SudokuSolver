from abc import ABC, abstractmethod

import numpy as np


class DigitRecognizer(ABC):
    @abstractmethod
    def recognize(self, cell: np.ndarray) -> int | None:
        pass