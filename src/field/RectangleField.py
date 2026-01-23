from src.cell.CellInteface import CellInterface
from src.field.RectangleFieldInterface import RectangleFieldInterface
from src.grid.Grid import Grid
from src.grid.GridInterface import GridInterface
from src.line.Line import Line
from src.unit.Coordinate import Coordinate


class RectangleField(RectangleFieldInterface):
    size: tuple[int, int]
    grids: dict[tuple[int, int], GridInterface]

    def __init__(self, size: tuple[int, int]) -> None:
        self.size = size
        self.grids = {}

        for x in range(1, size[0] + 1):
            for y in range(1, size[1] + 1):
                self.grids[x, y] = Grid(size)

    def get_size(self) -> tuple[int, int]:
        return self.size

    def get_grid(self, coordinate: Coordinate) -> GridInterface:
        if coordinate.to_tuple() in self.grids:
            return self.grids[*coordinate]

        raise IndexError("Coordinate out of bounds")

    def get_cell(self, coordinate: Coordinate) -> CellInterface | None:
        x, y = (coordinate.x - 1) // self.size[0] + 1, (coordinate.y - 1) // self.size[1] + 1
        grid_x, grid_y = (coordinate.x - 1) % self.size[0] + 1, (coordinate.y - 1) % self.size[1] + 1

        return self.grids[x, y].get_cell(Coordinate(grid_x, grid_y))

    def get_vertical_line(self, number: int) -> Line:
        if 1 <= number <= self.size[0] * self.size[1]:
            x = (number - 1) // self.size[0] + 1
            grid_x = (number - 1) % self.size[0] + 1

            line = Line(self.size[0] * self.size[0])

            for y in range(1, self.size[1] + 1):
                grid = self.get_grid(Coordinate(x, y))

                for grid_y in range(1, self.size[0] + 1):
                    grid_cell = grid.get_cell(Coordinate(grid_x, grid_y))
                    line.set_cell((y - 1) * self.size[1] + grid_y, grid_cell)

            return line

        raise IndexError("Number vertical line out of bounds")

    def get_horizontal_line(self, number: int) -> Line:
        if 1 <= number <= self.size[0] * self.size[1]:
            y = (number - 1) // self.size[1] + 1
            grid_y = (number - 1) % self.size[1] + 1

            line = Line(self.size[0] * self.size[0])

            for x in range(1, self.size[1] + 1):
                grid = self.get_grid(Coordinate(x, y))

                for grid_x in range(1, self.size[0] + 1):
                    grid_cell = grid.get_cell(Coordinate(grid_x, grid_y))
                    line.set_cell((x - 1) * self.size[0] + grid_x, grid_cell)

            return line

        raise IndexError(f"Number vertical line out of bounds({number})")

    def check_correct(self) -> bool:
        for grid in self.grids.values():
            if not grid.check_correct():
                return False

        return self.check_correct_vertical_lines() and self.check_correct_horizontal_lines()

    def check_correct_vertical_lines(self):
        for x in range(1, self.size[0] + 1):
            if not self.get_vertical_line(x).check_correct():
                return False

        return True

    def check_correct_horizontal_lines(self):
        for y in range(1, self.size[0] + 1):
            if not self.get_horizontal_line(y).check_correct():
                return False

        return True

    def check_final(self) -> bool:
        for grid in self.grids.values():
            if not grid.check_final():
                return False

        return self.check_correct()

    def __str__(self) -> str:
        result = ""

        for y in range(1, self.size[1] + 1):
            result += "\n+" + (("-" * (self.size[0] * 2 + 1)) + "+") * self.size[0]
            for grid_y in range(1, self.size[1] + 1):
                result += "\n"
                for x in range(1, self.size[0] + 1):
                    result += "| "
                    grid = self.get_grid(Coordinate(x, y))

                    for grid_x in range(1, self.size[0] + 1):
                        cell = grid.get_cell(Coordinate(grid_x, grid_y))
                        result += str(" " if cell is None else str(cell)) + " "
                result += "|"
        result += "\n+" + (("-" * (self.size[0] * 2 + 1)) + "+") * self.size[0]

        return result.lstrip("\n")