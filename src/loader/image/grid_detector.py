import cv2
import numpy as np


class GridDetector:
    def detect_grid(self, image: np.ndarray) -> tuple[int, int, int, int]:
        blur = cv2.GaussianBlur(image, (9, 9), 0)
        thresh = cv2.adaptiveThreshold(
            blur,
            255,
            cv2.ADAPTIVE_THRESH_GAUSSIAN_C,
            cv2.THRESH_BINARY_INV,
            11,
            2,
        )

        contours, _ = cv2.findContours(
            thresh, cv2.RETR_EXTERNAL, cv2.CHAIN_APPROX_SIMPLE
        )

        if not contours:
            raise ValueError("Sudoku grid not found")

        biggest = max(contours, key=cv2.contourArea)
        return cv2.boundingRect(biggest)  # x, y, w, h