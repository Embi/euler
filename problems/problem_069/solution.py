import json
import time
import numpy as np
from functools import lru_cache
from typing import List
from multiprocessing import Pool

def get_primes(up_to: int) -> List[int]:
    primes = list(range(up_to + 1))
    primes[0], primes[1] = 0, 0
    for i in primes:
        if not i:
            continue
        for j in range(2, up_to//i + 1):
            primes[i*j] = 0
    primes = list(set(primes))
    primes.remove(0)
    return sorted(primes)

_PRIMES = get_primes(1000)

def solution() -> int:
    # We are essentially just looking for a number smaller or equal to
    # 1000000 with most prime factors
    result = 1
    for p in _PRIMES:
        if result * p > 1000000:
            return result
        result = result * p

cpu_s, wall_s = time.process_time(), time.time()
result = solution()
cpu_e, wall_e = time.process_time(), time.time()

cpu_time, wall_time = cpu_e - cpu_s, wall_e - wall_s
print(json.dumps({"solution": result, "cpu": cpu_time, "wall": wall_time}))
