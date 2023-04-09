import json
import time
import math
from typing import List

def primes(up_to: int) -> List[int]:
    candidates = list(range(up_to))
    limit = int(up_to**0.5)+1
    for i in candidates:
        if i in [0,1]:
            continue
        if i == limit:
            break
        for j in range(i*2, up_to, i):
            candidates[j] = 0
    candidates = set(candidates)
    candidates.remove(0)
    candidates.remove(1)
    return sorted(candidates)

_PRIMES = primes(2_000_000)

def is_prime(n: int) -> bool:
    limit = int(n**0.5)+1
    for prime in _PRIMES:
        if prime >= limit:
            return True
        if n%prime == 0:
            return False

def goldbach_valid(n):
    for i in range(int((n/2)**0.5)+1):
        if is_prime(n - 2*i**2):
            return True
    return False

def solution() -> int:
    for i in range(1, 2_000_000_000, 2):
        if is_prime(i):
            # Don't check primes
            continue
        if not goldbach_valid(i):
            return i

cpu_s, wall_s = time.process_time(), time.time()
result = solution()
cpu_e, wall_e = time.process_time(), time.time()

cpu_time, wall_time = cpu_e - cpu_s, wall_e - wall_s
print(json.dumps({"solution": result, "cpu": cpu_time, "wall": wall_time}))
