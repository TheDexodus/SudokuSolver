import cv2
import numpy as np

from src.cell.constant_cell import ConstantCell
from src.cell.empty_cell import EmptyCell
from src.coordinate.two_dimensional_coordinate import TwoDimensionalCoordinate
from src.field.rectangle_field import RectangleField
from src.loader.abstract_file_field_loader import AbstractFileFieldLoader
from src.loader.image.digit_recognizer_cnn import DigitRecognizerCNN


class ImageFileFieldLoader(AbstractFileFieldLoader):
    """
    Loader, который принимает путь к изображению судоку,
    находит сетку 9x9 и возвращает RectangleField
    """

    GRID_SIZE = 9
    SUBGRID_SIZE = 3

    def __init__(self, file_path):
        super().__init__(file_path)
        self.recognizer = DigitRecognizerCNN()

    def load(self) -> RectangleField:
        image = self._load_image()
        grid_rect = self._detect_grid(image)
        cells = self._extract_cells(image, grid_rect)
        values = self._recognize_digits(cells)

        return self._build_field(values)

    # ---------------------------------------------------------------------
    # Image loading
    # ---------------------------------------------------------------------

    def _load_image(self) -> np.ndarray:
        image = cv2.imread(str(self.file_path), cv2.IMREAD_GRAYSCALE)
        if image is None:
            raise ValueError(f"Cannot load image {self.file_path}")
        return image

    # ---------------------------------------------------------------------
    # Grid detection
    # ---------------------------------------------------------------------

    def _detect_grid(self, image: np.ndarray) -> tuple[int, int, int, int]:
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

    # ---------------------------------------------------------------------
    # Cell extraction
    # ---------------------------------------------------------------------

    def _extract_cells(
        self,
        image: np.ndarray,
        grid_rect: tuple[int, int, int, int],
    ) -> dict[tuple[int, int], np.ndarray]:
        x, y, w, h = grid_rect

        cell_w = w // self.GRID_SIZE
        cell_h = h // self.GRID_SIZE

        margin_w = int(cell_w * 0.1)
        margin_h = int(cell_h * 0.1)

        cells: dict[tuple[int, int], np.ndarray] = {}

        for row in range(self.GRID_SIZE):
            for col in range(self.GRID_SIZE):
                cx = x + col * cell_w
                cy = y + row * cell_h

                cell = image[
                    cy + margin_h : cy + cell_h - margin_h,
                    cx + margin_w : cx + cell_w - margin_w,
                ]

                cells[(col, row)] = cell

        return cells

    # ---------------------------------------------------------------------
    # Digit recognition (MVP)
    # ---------------------------------------------------------------------

    def _recognize_digits(
        self,
        cells: dict[tuple[int, int], np.ndarray],
    ) -> dict[tuple[int, int], int | None]:
        values = {}

        for (x, y), cell in cells.items():
            # cv2.imwrite(
            #     f"debug/cell_{y}_{x}.png",
            #     cell
            # )
            values[(x, y)] = self.recognizer.recognize(cell)

        return values

    def _is_empty(self, cell: np.ndarray) -> bool:
        _, thresh = cv2.threshold(cell, 0, 255, cv2.THRESH_BINARY_INV + cv2.THRESH_OTSU)
        return cv2.countNonZero(thresh) < 50

    # ---------------------------------------------------------------------
    # Field building
    # ---------------------------------------------------------------------

    def _build_field(
        self,
        values: dict[tuple[int, int], int | None],
    ) -> RectangleField:
        field = RectangleField((self.SUBGRID_SIZE, self.SUBGRID_SIZE))

        for (x, y), value in values.items():
            grid_coord = TwoDimensionalCoordinate(
                x // self.SUBGRID_SIZE + 1,
                y // self.SUBGRID_SIZE + 1,
            )

            cell_coord = TwoDimensionalCoordinate(
                x % self.SUBGRID_SIZE + 1,
                y % self.SUBGRID_SIZE + 1,
            )

            grid = field.get_grid(grid_coord)

            grid.set_cell(
                cell_coord,
                EmptyCell() if value is None else ConstantCell(value),
            )

        return field