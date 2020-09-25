from operator import add
from random import choice, randrange
from typing import List, Tuple, Optional

_Field = List[List[bool]]
_Vector2i = Tuple[int, int]
is_debug: bool = False


# noinspection PyTypeChecker
def _vector_add(a: _Vector2i, b: _Vector2i) -> _Vector2i:
    return tuple(map(add, a, b))


def _run(size_of_field: int) -> bool:
    # тут создается квадрат
    field = [[False for _ in range(size_of_field)] for _ in range(size_of_field)]
    current_point: _Vector2i = randrange(size_of_field), randrange(size_of_field)
    x, y = current_point
    # черепашка помещается на x, y
    field[x][y] = True

    while True:
        increment: _Vector2i
        is_outside: bool
        increment, is_outside = _choose_direction(current_point, field)

        if is_outside:
            # выход из города
            return True  # вышла из города

        if increment is None:
            return False  # попала в тупик

        current_point = _vector_add(current_point, increment)
        x, y = current_point
        # черепашка помещается на x, y
        field[x][y] = True

        if is_debug:
            print("".join(["".join(
                ["O" if idx_x == current_point[0] and idx_y == current_point[1] else "*" if value else "+" for
                 idx_y, value in enumerate(line)]) + "\n" for idx_x, line in enumerate(field)]))


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


def solution(n_times: int, size_of_field: int) -> float:
    counter = 0

    for i in range(n_times):
        if _run(size_of_field):
            counter += 1

    return float(counter) / n_times
