from src.cell.CandidateCell import CandidateCell
from src.loader.TxtFileFieldLoader import TxtFileFieldLoader
from src.possible.PossibleHelper import PossibleHelper
from src.solver.RectangleSolver import RectangleSolver
from src.unit.Coordinate import Coordinate

file_loader = TxtFileFieldLoader("tasks/task1.txt")
field = file_loader.load()

print(field)
print("Correct" if field.check_correct() else "Incorrect")

solver = RectangleSolver()
solver.solve(field)
print(field)

cell1 = field.get_cell(Coordinate(5, 1))
cell2 = field.get_cell(Coordinate(6, 2))
cell3 = field.get_cell(Coordinate(5, 3))

if isinstance(cell1, CandidateCell):
    print(cell1.get_possible_values())

print(PossibleHelper.get_possible_cell(field.get_grid(Coordinate(2, 1))).get_possible_values())