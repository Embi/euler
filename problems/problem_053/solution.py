import json
import time
from functools import reduce


def get_comb_count(n: int, r: int):
    """Get number of combinations for given n and r
    """
    numerator = reduce(lambda x, y: x*y, range(n-r+1, n+1))
    denominator = reduce(lambda x, y: x*y, range(1, r+1))
    return numerator // denominator


def solution() -> int:
    above_mil = 0
    for n in range(1, 101):
        odd = n%2
        n_above_mil = 0
        for r in range(n//2, 1, -1):
            comb_count = get_comb_count(n, r)
            if comb_count > 1_000_000:
                if not odd and r == n//2:
                    n_above_mil += 1
                else:
                    n_above_mil += 2
        above_mil += n_above_mil
    return above_mil

cpu_s, wall_s = time.process_time(), time.time()
result = solution()
cpu_e, wall_e = time.process_time(), time.time()

cpu_time, wall_time = cpu_e - cpu_s, wall_e - wall_s
print(json.dumps({"solution": result, "cpu": cpu_time, "wall": wall_time}))
