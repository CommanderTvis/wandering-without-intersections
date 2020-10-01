from turtle import Turtle, Screen

from main import run, Vector2i

_turtle: Turtle = Turtle()
_screen: Screen = Screen()
_dpi: int = 30
_size_of_field_input: int = int(_screen.textinput("Size of field", "Enter the size of field: "))
_side = _size_of_field_input * _dpi
_turtle.goto(0, _side)
_turtle.goto(_side, _side)
_turtle.goto(_side, 0)
_turtle.goto(0, 0)


def _handler(current_point: Vector2i, initial: bool) -> None:
    if initial:
        _turtle.penup()
        _turtle.goto(current_point[0] * _dpi, current_point[1] * _dpi)
        _turtle.pendown()
        return

    _turtle.goto(current_point[0] * _dpi, current_point[1] * _dpi)
    pass


run(_size_of_field_input, _handler)
_screen.mainloop()
