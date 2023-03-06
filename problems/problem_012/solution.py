import json
import time
import numpy as np
import itertools as it

_FACTORS = {}

def _factors(n: int) -> [int]:
    if n in _FACTORS:
        return _FACTORS[n]
    factors = np.array([1,n])
    for i in range(2, n//2+1):
        if n % i == 0:
            cached_factors = _factors(n//i)
            factors = np.concatenate((
                factors, cached_factors, i*cached_factors))
            factors = np.unique(factors)
            break
    factors = np.unique(factors)
    _FACTORS[n] = factors
    return factors

def _triangle_sequence():
    triang_number = 0
    for num in it.count(start=1):
        triang_number += num
        yield triang_number


def solution() -> int:
    for triang_number in _triangle_sequence():
        factors = _factors(triang_number)
        f_count = len(factors)
        if f_count >= 500:
            return triang_number

cpu_s, wall_s = time.process_time(), time.time()
result = solution()
cpu_e, wall_e = time.process_time(), time.time()

cpu_time, wall_time = cpu_e - cpu_s, wall_e - wall_s
print(json.dumps({"solution": result, "cpu": cpu_time, "wall": wall_time}))
