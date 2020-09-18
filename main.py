from typing import List, Tuple

field: List[List[bool]]
currentPoint: Tuple[int, int]


# присваивает в field двумерный список булев с size столбцов и size строк
def make_field(size: int) -> None:
    # TODO
    pass


# 1. создает поле.
# 2. выбирает случайную точку.
# 3. устанавливает currentPoint на эту точку.
# 4. циклически выбирает случайные вектора
# (до тех пор, как она не попадает в путик или не выйдет за пределы поля)
# 5. возвращает, попала ли собака в тупик (или вышла из "города")
def start() -> bool:
    # TODO
    pass


# возвращает случайный кортеж со случайными значениями вида (0, 1), (0, -1), (-1, 0), (1, 0)
def choose_direction() -> Tuple[int, int]:
    # TODO
    pass


# запускает start n_times раз, и возвращает отношение попаданий в тупик к количеству запусков
def solution(n_times: int) -> float:
    counter: int = 0

    for i in range(n_times):
        if start():
            counter += 1

    return counter / n_times
