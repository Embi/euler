import json
import time
from typing import List
from itertools import compress
import numpy as np

def get_primes_lookup(below: int) -> List[bool]:
    primes = np.ones(below, dtype=np.uint8)
    primes[0], primes[1] = 0, 0
    for i in range(2, int(below**0.5)+1):
        if not primes[i]:
            continue
        for j in range(2, below // i + 1):
            try:
                primes[i*j] = 0
            except IndexError:
                break
    return primes

PRIMES_LOOKUP = get_primes_lookup(100_000_000)

def get_primes(below: int) -> List[int]:
    primes = []
    for idx, is_prime in enumerate(PRIMES_LOOKUP):
        if idx == below:
            return primes
        if is_prime:
            primes.append(idx)


def is_remarkable(prime_set, prime) -> bool:
    for p in prime_set:
        con1, con2 = int(str(p)+str(prime)), int(str(prime)+str(p))
        if not PRIMES_LOOKUP[con1] or not PRIMES_LOOKUP[con2]:
            return False
    return True

def solution() -> int:
    primes = get_primes(10000)
    sets = [(p,) for p in primes]
    for i in range(4):
        _sets = []
        for s in sets:
            max_p = max(s)
            for p in primes:
                if p < max_p:
                    continue
                if is_remarkable(s, p):
                    _sets.append(tuple(sorted(s + (p,))))
        sets = sorted(list(set(_sets)))
    return sum(sets[0])

cpu_s, wall_s = time.process_time(), time.time()
result = solution()
cpu_e, wall_e = time.process_time(), time.time()

cpu_time, wall_time = cpu_e - cpu_s, wall_e - wall_s
print(json.dumps({"solution": result, "cpu": cpu_time, "wall": wall_time}))
