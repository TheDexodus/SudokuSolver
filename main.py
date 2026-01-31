import pygame

from src.loader.txt_file_field_loader import TxtFileFieldLoader
from src.solver.rectangle_solver import RectangleSolver
from src.ui.FieldDrawer import FieldDrawer

SUDOKU_FILENAME = "tasks/task4.txt"

file_loader = TxtFileFieldLoader(SUDOKU_FILENAME)
field = file_loader.load()

solver = RectangleSolver()
field = solver.solve(field)
print(field)

pygame.init()
screen = pygame.display.set_mode((600, 600))
pygame.display.set_caption("Sudoku")
field_drawer = FieldDrawer()

clock = pygame.time.Clock()
running = True

while running:
    for event in pygame.event.get():
        if event.type == pygame.QUIT:
            running = False

    field_drawer.draw(screen, field)
    pygame.display.flip()
    clock.tick(60)