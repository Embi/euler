import json
import time
from itertools import count, islice
from typing import Iterator, Tuple

def get_e_cont_frac() -> Iterator[int]:
    """Get continued fraction for e
    """
    for i in count(1):
        yield 1
        yield 2*i
        yield 1

def get_nth_convergent(nth: int) -> Tuple[int, int]:
    """Get numerator and denominator for nth convergent
    """
    n, d = 0, 1
    for i in reversed(list(islice(get_e_cont_frac(), nth-1))):
        n, d = d, d*i + n
    return n+2*d, d

def solution() -> int:
    n, d = get_nth_convergent(100)
    return sum(int(i) for i in str(n))

cpu_s, wall_s = time.process_time(), time.time()
result = solution()
cpu_e, wall_e = time.process_time(), time.time()

cpu_time, wall_time = cpu_e - cpu_s, wall_e - wall_s
print(json.dumps({"solution": result, "cpu": cpu_time, "wall": wall_time}))
