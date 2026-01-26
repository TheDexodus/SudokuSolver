from src.loader.txt_file_field_loader import TxtFileFieldLoader
from src.solver.rectangle_solver import RectangleSolver

file_loader = TxtFileFieldLoader("tasks/task1.txt")
field = file_loader.load()

solver = RectangleSolver()
solver.solve(field)
print(field)
