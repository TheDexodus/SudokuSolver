from src.field.line_builder import LineBuilder
from src.field.rectangle_field import RectangleField


class RectangleFieldHelper:
    @classmethod
    def rotate_field_clockwise(cls, field: RectangleField) -> RectangleField:
        new_size = field.get_size()[1], field.get_size()[0]
        new_field = RectangleField(new_size)

        for row_order, row_line in enumerate(LineBuilder.build_all_row_lines(field), 1):
            LineBuilder.insert_column_line(new_field, row_line, field.get_size()[0] * field.get_size()[1] - row_order + 1)

        return new_field

    @classmethod
    def rotate_field_counterclockwise(cls, field: RectangleField) -> RectangleField:
        new_size = field.get_size()[1], field.get_size()[0]
        new_field = RectangleField(new_size)

        for column_order, column_line in enumerate(LineBuilder.build_all_column_lines(field), 1):
            LineBuilder.insert_row_line(new_field, column_line, field.get_size()[0] * field.get_size()[1] - column_order + 1)

        return new_field