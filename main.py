from random import randrange
from typing import List, Tuple, Optional

_Field = List[List[bool]]
_Vector2i = Tuple[int, int]
_is_debug: bool = False


def _vector_add(a: _Vector2i, b: _Vector2i) -> _Vector2i:
    return a[0] + b[0], a[1] + b[1]


def _run(size_of_field: int) -> bool:
    field = []

    for _ in range(size_of_field):
        l = []

        for _ in range(size_of_field):
            l.append(False)

        field.append(l)

    current_point: _Vector2i = randrange(size_of_field), randrange(size_of_field)
    # TODO
    pass


_directions: List[_Vector2i] = [(0, 1), (0, -1), (-1, 0), (1, 0)]


def _choose_direction(current_point: _Vector2i, field: _Field) -> Tuple[Optional[_Vector2i], bool]:
    # TODO
    pass


def _solution(n_times: int, size_of_field: int) -> float:
    counter = 0

    for i in range(n_times):
        if _run(size_of_field):
            counter += 1

    return float(counter) / n_times


_is_debug_input = input("Turn on debug mode (y/n)? ")

if _is_debug_input == "y":
    _is_debug = True

_n_times_input = int(input("Enter the quantity of times to run the algorithm: "))
_size_of_field_input = int(input("Enter the size of field: "))
_probability = _solution(_n_times_input, _size_of_field_input)
print(f"The posterior probability of escaping the field is {_probability}")
