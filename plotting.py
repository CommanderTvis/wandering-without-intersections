from typing import List

from matplotlib.pyplot import *
from main import solution

_n_times: int = 300
_x: range = range(1, 101, 3)
_y: List[float] = list(map(lambda x: solution(_n_times, x), _x))
print("data is ready")
plot(_x, _y)
show()
