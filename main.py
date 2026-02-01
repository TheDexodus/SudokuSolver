import pygame

from src.loader.image_field_loader import ImageFileFieldLoader
from src.solver.rectangle_solver import RectangleSolver
from src.ui.FieldDrawer import FieldDrawer

SUDOKU_FILENAME = "tasks/img.png"

loader = ImageFileFieldLoader(SUDOKU_FILENAME)
field = loader.load()

solver = RectangleSolver()
field = solver.solve(field)
print(field)

pygame.init()
screen = pygame.display.set_mode((600, 600))
pygame.display.set_caption("Sudoku")
field_drawer = FieldDrawer(cell_size=40)

clock = pygame.time.Clock()
running = True

field_drawer.draw(screen, field)
pygame.display.flip()

while running:
    for event in pygame.event.get():
        if event.type == pygame.QUIT:
            running = False

    clock.tick(60)