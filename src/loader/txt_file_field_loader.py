from src.cell.constant_cell import ConstantCell
from src.cell.empty_cell import EmptyCell
from src.coordinate.two_dimensional_coordinate import TwoDimensionalCoordinate
from src.field.rectangle_field import RectangleField
from src.loader.abstract_file_field_loader import AbstractFileFieldLoader


class TxtFileFieldLoader(AbstractFileFieldLoader):
    field_size: tuple[int, int] | None = None

    def load(self) -> RectangleField:
        field = RectangleField(self.get_field_size())

        for coordinate, value in self.get_values().items():
            grid_coordinate = TwoDimensionalCoordinate(coordinate.get_x() // self.field_size[1] + 1,
                                                       coordinate.get_y() // self.field_size[0] + 1)
            grid = field.get_grid(grid_coordinate)
            cell_coordinate = TwoDimensionalCoordinate(coordinate.get_x() % self.field_size[1] + 1,
                                                       coordinate.get_y() % self.field_size[0] + 1)

            grid.set_cell(cell_coordinate, EmptyCell() if value is None else ConstantCell(value))

        return field

    def get_field_size(self) -> tuple[int, int]:
        if self.field_size is None:
            with self.file_path.open("r", encoding="utf-8") as file:
                first_line = file.readline()
                field_size_x = first_line.count("+") - 1

            with self.file_path.open("r", encoding="utf-8") as file:
                field_size_y = -1

                for line in file:
                    if line.startswith("+"):
                        field_size_y += 1

            self.field_size = field_size_x, field_size_y

        return self.field_size

    def get_values(self) -> dict[TwoDimensionalCoordinate, int | None]:
        values: dict[TwoDimensionalCoordinate, int | None] = {}

        with self.file_path.open("r", encoding="utf-8") as file:
            y = 0

            for line in file:
                line = line.rstrip("\n")

                if line.startswith("+"):
                    continue

                x = 0
                i = 0
                for char in line:
                    i += 1

                    if char == "|" or i % 2 == 0:
                        continue

                    if char == " ":
                        values[TwoDimensionalCoordinate(x, y)] = None
                        x += 1
                    elif char.isdigit():
                        values[TwoDimensionalCoordinate(x, y)] = int(char)
                        x += 1

                y += 1

        return values