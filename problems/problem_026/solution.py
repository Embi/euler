import json
import time
from typing import Dict, List, Tuple

def fraction_cycle(n: int) -> int:
    """compute fraction cycle length for numerator 1 and denumerator n
    """
    fractions: Dict[Tuple[int, int], int] = {}
    numerator: int = 1
    idx = 0
    while numerator != 0:
        numerator *= 10
        fraction = numerator // n
        if (numerator, n) in fractions:
            return idx - fractions[(numerator, n)]
        fractions[(numerator, n)] = idx
        numerator %= n
        idx += 1
    return 0


def find_max_cycle(max_denom: int) -> int:
    max_cycle = 0
    max_cycle_denominator = 0
    for i in range(1, max_denom):
        cycle = fraction_cycle(i)
        if cycle > max_cycle:
            max_cycle = cycle
            max_cycle_denominator = i
    return max_cycle_denominator


def solution() -> int:
    return find_max_cycle(1000)


cpu_s, wall_s = time.process_time(), time.time()
result = solution()
cpu_e, wall_e = time.process_time(), time.time()

cpu_time, wall_time = cpu_e - cpu_s, wall_e - wall_s
print(json.dumps({"solution": result, "cpu": cpu_time, "wall": wall_time}))
