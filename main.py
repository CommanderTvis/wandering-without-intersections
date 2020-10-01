from operator import add
from random import choice, randrange
from typing import List, Tuple, Optional, Callable

_Field = List[List[bool]]
Vector2i = Tuple[int, int]
is_debug: bool = False


# noinspection PyTypeChecker
def _vector_add(a: Vector2i, b: Vector2i) -> Vector2i:
    return tuple(map(add, a, b))


def run(size_of_field: int, on_moved: Callable[[Vector2i, bool], None] = lambda x: None) -> bool:
    field = [[False for _ in range(size_of_field)] for _ in range(size_of_field)]
    current_point = randrange(size_of_field), randrange(size_of_field)
    on_moved(current_point, True)
    x, y = current_point
    field[x][y] = True

    while True:
        increment, is_outside = _choose_direction(current_point, field)

        if is_outside:
            return True  # вышла из города

        if increment is None:
            return False  # попала в тупик

        current_point = _vector_add(current_point, increment)
        x, y = current_point
        on_moved(current_point, False)
        field[x][y] = True

        if is_debug:
            print("".join(["".join(
                ["O" if idx_x == current_point[0] and idx_y == current_point[1] else "*" if value else "+" for
                 idx_y, value in enumerate(line)]) + "\n" for idx_x, line in enumerate(field)]))


_directions: List[Vector2i] = [(0, 1), (0, -1), (-1, 0), (1, 0)]


def _choose_direction(current_point: Vector2i, field: _Field) -> Tuple[Optional[Vector2i], bool]:
    not_visited = []

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


def probability(n_times: int, size_of_field: int) -> float:
    counter = 0

    for i in range(n_times):
        if run(size_of_field):
            counter += 1

    return float(counter) / n_times
