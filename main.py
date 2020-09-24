from operator import add
from random import randrange, choice
from typing import List, Tuple, Optional

_Field = List[List[bool]]
_Vector2i = Tuple[int, int]
_is_debug: bool = False


# noinspection PyTypeChecker
def _vector_add(a: _Vector2i, b: _Vector2i) -> _Vector2i:
    return tuple(map(add, a, b))


def _run(size_of_field: int) -> bool:
    field = [[False for _ in range(size_of_field)] for _ in range(size_of_field)]
    current_point: _Vector2i = randrange(size_of_field), randrange(size_of_field)
    x, y = current_point
    field[x][y] = True
    # TODO
    pass


_directions: List[_Vector2i] = [(0, 1), (0, -1), (-1, 0), (1, 0)]


def _choose_direction(current_point: _Vector2i, field: _Field) -> Tuple[Optional[_Vector2i], bool]:
    not_visited: List[Tuple[Optional[_Vector2i], bool]] = []

    for i in _directions:
        xi, yi = _vector_add(current_point, i)

        if xi >= len(field) or yi >= len(field) or xi < 0 or yi < 0:
            not_visited.append((None, True))
            continue

        if not field[xi][yi]:
            not_visited.append((i, False))

    if not not_visited:
        return None, False

    return choice(not_visited)


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
