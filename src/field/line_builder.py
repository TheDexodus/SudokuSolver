from src.coordinate.ordinal_coordinate import OrdinalCoordinate
from src.coordinate.two_dimensional_coordinate import TwoDimensionalCoordinate
from src.field.field import Field
from src.repository.line_cell_repository import LineCellRepository


class LineBuilder:
    @classmethod
    def build_vertical_line(cls, field: Field, order: int) -> LineCellRepository:
        line = LineCellRepository(field.get_size()[1] ** 2)
        grid_x = (order - 1) % 3 + 1
        cell_x = (order - 1) // 3 + 1

        for grid_y in range(1, field.get_size()[1] + 1):
            grid = field.get_grid(TwoDimensionalCoordinate(grid_x, grid_y))

            for cell_y in range(1, grid.get_size()[1] + 1):
                cell = grid.get_cell(TwoDimensionalCoordinate(cell_x, cell_y))
                line.set_cell(OrdinalCoordinate((grid_y - 1) * 3 + cell_y), cell)

        return line

    @classmethod
    def build_horizontal_line(cls, field: Field, order: int) -> LineCellRepository:
        line = LineCellRepository(field.get_size()[0] ** 2)
        grid_y = (order - 1) % 3 + 1
        cell_y = (order - 1) // 3 + 1

        for grid_x in range(1, field.get_size()[0] + 1):
            grid = field.get_grid(TwoDimensionalCoordinate(grid_x, grid_y))

            for cell_x in range(1, grid.get_size()[0] + 1):
                cell = grid.get_cell(TwoDimensionalCoordinate(cell_x, cell_y))
                line.set_cell(OrdinalCoordinate((grid_x - 1) * 3 + cell_x), cell)

        return line

    @classmethod
    def build_all_vertical_lines(cls, field: Field) -> list[LineCellRepository]:
        lines: list[LineCellRepository] = []

        for order in range(1, field.get_size()[0] + 1):
            lines.append(cls.build_vertical_line(field, order))

        return lines

    @classmethod
    def build_all_horizontal_lines(cls, field: Field) -> list[LineCellRepository]:
        lines: list[LineCellRepository] = []

        for order in range(1, field.get_size()[0] + 1):
            lines.append(cls.build_horizontal_line(field, order))

        return lines

    @classmethod
    def insert_horizontal_line(cls, field: Field, line: LineCellRepository, order: int) -> Field:
        grid_y = (order - 1) // 3 + 1
        cell_y = (order - 1) % 3 + 1

        for i in range(1, line.get_count_cells() + 1):
            line_cell = line.get_cell(OrdinalCoordinate(i))

            grid_x = (i - 1) // 3 + 1
            cell_x = (i - 1) % 3 + 1

            grid = field.get_grid(TwoDimensionalCoordinate(grid_x, grid_y))
            if grid.get_cell(TwoDimensionalCoordinate(cell_x, cell_y)).can_be_replaced():
                grid.set_cell(TwoDimensionalCoordinate(cell_x, cell_y), line_cell)

        return field

    @classmethod
    def insert_vertical_line(cls, field: Field, line: LineCellRepository, order: int) -> Field:
        grid_x = (order - 1) // 3 + 1
        cell_x = (order - 1) % 3 + 1

        for i in range(1, line.get_count_cells() + 1):
            line_cell = line.get_cell(OrdinalCoordinate(i))

            grid_y = (i - 1) // 3 + 1
            cell_y = (i - 1) % 3 + 1

            grid = field.get_grid(TwoDimensionalCoordinate(grid_x, grid_y))
            if grid.get_cell(TwoDimensionalCoordinate(cell_x, cell_y)).can_be_replaced():
                grid.set_cell(TwoDimensionalCoordinate(cell_x, cell_y), line_cell)

        return field