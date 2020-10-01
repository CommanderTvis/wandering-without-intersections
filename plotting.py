from typing import List

from matplotlib.pyplot import *
from main import probability

_n_times: int = 1000
_x: range = range(1, 101, 5)
_y: List[float] = list(map(lambda x: probability(_n_times, x), _x))
print("data is ready")
plot(_x, _y)
show()
