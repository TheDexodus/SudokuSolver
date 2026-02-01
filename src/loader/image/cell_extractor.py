import numpy as np


class CellExtractor:
    GRID_SIZE = 9

    def extract_cells(self, image: np.ndarray, grid_rect: tuple[int, int, int, int]) -> dict[tuple[int, int], np.ndarray]:
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