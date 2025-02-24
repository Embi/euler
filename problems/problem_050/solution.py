import json
import time
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

_PRIMES = primes(1_000_000)
_PRIMES_LOOKUP = set(_PRIMES)

def solution() -> int:
    max_consec_len = 0
    max_consec_sum = 0
    for i in range(len(_PRIMES)):
        if i > 47000:
            break
        consec_sum = 0
        consec_len = 0
        for j in range(i+1, len(_PRIMES)):
            consec_sum += _PRIMES[j]
            consec_len += 1
            if consec_sum > 1_000_000:
                break
            if consec_sum in _PRIMES_LOOKUP:
                if consec_len > max_consec_len:
                    max_consec_len = consec_len
                    max_consec_sum = consec_sum
    return max_consec_sum

cpu_s, wall_s = time.process_time(), time.time()
result = solution()
cpu_e, wall_e = time.process_time(), time.time()

cpu_time, wall_time = cpu_e - cpu_s, wall_e - wall_s
print(json.dumps({"solution": result, "cpu": cpu_time, "wall": wall_time}))
