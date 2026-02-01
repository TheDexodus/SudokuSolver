import os

import cv2
import numpy as np
import tensorflow as tf

from src.loader.image.digit_recognizer import DigitRecognizer


class DigitRecognizerCNN(DigitRecognizer):
    MODEL_PATH = os.path.join("models", "digit_cnn_model.keras")
    EMPTY_THRESHOLD = 40

    def __init__(self):
        self.model = self._load_model()

    def recognize(self, cell: np.ndarray) -> int | None:
        image = self._prepare(cell)

        if self._is_empty(image):
            return None

        prediction = self.model.predict(image, verbose=0)
        digit = int(np.argmax(prediction))

        if digit == 0:
            return None

        return digit

    def _prepare(self, cell: np.ndarray) -> np.ndarray:
        h, w = cell.shape
        margin = int(min(h, w) * 0.15)

        cell = cell[
            margin : h - margin,
            margin : w - margin,
        ]

        # Binarize
        _, cell = cv2.threshold(
            cell,
            0,
            255,
            cv2.THRESH_BINARY_INV + cv2.THRESH_OTSU
        )

        # Resize to 28x28
        cell = cv2.resize(cell, (28, 28))

        # Center the digit using image moments
        M = cv2.moments(cell)
        if M["m00"] > 0:
            cx = int(M["m10"] / M["m00"])
            cy = int(M["m01"] / M["m00"])
            shift_x = 14 - cx
            shift_y = 14 - cy
            # Affine translation matrix
            M_shift = np.float32([[1, 0, shift_x], [0, 1, shift_y]])
            cell = cv2.warpAffine(cell, M_shift, (28, 28), flags=cv2.INTER_LINEAR, borderValue=0)

        cell = cell.astype("float32") / 255.0

        return cell.reshape(1, 28, 28, 1)

    def _is_empty(self, image: np.ndarray) -> bool:
        return np.sum(image) < self.EMPTY_THRESHOLD

    def _load_model(self) -> tf.keras.Model:
        if not os.path.exists(self.MODEL_PATH):
            raise FileNotFoundError(f"Model not found at {self.MODEL_PATH}. Train it first.")
        return tf.keras.models.load_model(self.MODEL_PATH)