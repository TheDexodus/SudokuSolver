import pygame

from src.cell.candidate_cell import CandidateCell
from src.coordinate.two_dimensional_coordinate import TwoDimensionalCoordinate
from src.field.field import Field


class FieldDrawer:
    def __init__(
        self,
        cell_size: int = 60,
        margin: int = 20,
        line_color=(0, 0, 0),
        bg_color=(255, 255, 255),
        number_color=(0, 0, 0),
        bold_line_width: int = 4,
        thin_line_width: int = 1,
    ):
        self.cell_size = cell_size
        self.margin = margin
        self.line_color = line_color
        self.bg_color = bg_color
        self.number_color = number_color
        self.bold_line_width = bold_line_width
        self.thin_line_width = thin_line_width

        pygame.font.init()
        self.font = pygame.font.SysFont("arial", int(cell_size * 0.6))
        self.candidate_font = pygame.font.SysFont(
            "arial", int(cell_size * 0.25)
        )
        self.candidate_color = (150, 150, 150)

    def draw(self, screen: pygame.Surface, field: Field) -> None:
        screen.fill(self.bg_color)

        self._draw_grid(screen, field.get_size())
        self._draw_numbers(screen, field)

    def _draw_grid(self, screen: pygame.Surface, size: tuple[int, int]) -> None:
        grids_x, grids_y = size

        cells_in_row = grids_y
        cells_in_col = grids_x

        total_cells_x = grids_x * cells_in_row
        total_cells_y = grids_y * cells_in_col

        start_x = self.margin
        start_y = self.margin

        width = total_cells_x * self.cell_size
        height = total_cells_y * self.cell_size

        # vertical lines
        for x in range(total_cells_x + 1):
            line_width = (
                self.bold_line_width if x % cells_in_row == 0 else self.thin_line_width
            )
            px = start_x + x * self.cell_size
            pygame.draw.line(
                screen,
                self.line_color,
                (px, start_y),
                (px, start_y + height),
                line_width,
            )

        # horizontal lines
        for y in range(total_cells_y + 1):
            line_width = (
                self.bold_line_width if y % cells_in_col == 0 else self.thin_line_width
            )
            py = start_y + y * self.cell_size
            pygame.draw.line(
                screen,
                self.line_color,
                (start_x, py),
                (start_x + width, py),
                line_width,
            )

    def _draw_numbers(self, screen: pygame.Surface, field: Field) -> None:
        start_x = self.margin
        start_y = self.margin

        for row in range(1, field.get_size()[0] * field.get_size()[1] + 1):
            for col in range(1, field.get_size()[0] * field.get_size()[1] + 1):
                grid_x = (col - 1) // field.get_size()[1] + 1
                grid_y = (row - 1) // field.get_size()[0] + 1
                cell_x = (col - 1) % field.get_size()[1] + 1
                cell_y = (row - 1) % field.get_size()[0] + 1

                cell = field.get_grid(TwoDimensionalCoordinate(grid_x, grid_y)).get_cell(TwoDimensionalCoordinate(cell_x, cell_y))
                value = cell.get_value()

                if isinstance(cell, CandidateCell):
                    possible_values = cell.get_possible_values()
                    if not possible_values:
                        continue

                    sub_cell_size = self.cell_size // field.get_size()[0]

                    for value in possible_values:
                        sub_x = (value - 1) % field.get_size()[1]
                        sub_y = (value - 1) // field.get_size()[0]

                        text_surface = self.candidate_font.render(
                            str(value), True, self.candidate_color
                        )
                        text_rect = text_surface.get_rect()

                        pixel_x = (
                            start_x
                            + (col - 1) * self.cell_size
                            + sub_x * sub_cell_size
                            + sub_cell_size // 2
                        )
                        pixel_y = (
                            start_y
                            + (row - 1) * self.cell_size
                            + sub_y * sub_cell_size
                            + sub_cell_size // 2
                        )

                        text_rect.center = (pixel_x, pixel_y)
                        screen.blit(text_surface, text_rect)
                else:
                    if value is None or value == 0:
                        continue

                    text_surface = self.font.render(str(value), True, self.number_color)
                    text_rect = text_surface.get_rect()

                    cell_x = start_x + (col - 1) * self.cell_size
                    cell_y = start_y + (row - 1) * self.cell_size

                    text_rect.center = (
                        cell_x + self.cell_size // 2,
                        cell_y + self.cell_size // 2,
                    )

                    screen.blit(text_surface, text_rect)