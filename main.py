from typing import List, Tuple, Optional

Field = List[List[bool]]
Vector2i = Tuple[int, int]
is_debug: bool = False


def _vector_add(a: Vector2i, b: Vector2i) -> Vector2i:
    # TODO
    pass


def _run(size_of_field: int) -> bool:
    # TODO
    pass


_directions: List[Vector2i] = [(0, 1), (0, -1), (-1, 0), (1, 0)]


def _choose_direction(current_point: Vector2i, field: Field) -> Tuple[Optional[Vector2i], bool]:
    # TODO
    pass


def _solution(n_times: int, size_of_field: int) -> float:
    counter = 0

    for i in range(n_times):
        if _run(size_of_field):
            counter += 1

    return float(counter) / n_times


is_debug_input = input("Turn on debug mode (y/n)? ")

if is_debug_input == "y":
    is_debug = True

n_times_input = int(input("Enter the quantity of times to run the algorithm: "))
size_of_field_input = int(input("Enter the size of field: "))
probability = _solution(n_times_input, size_of_field_input)
print(f"The posterior probability is {probability}")
