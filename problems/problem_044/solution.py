import json
import time
from itertools import count
from typing import List
from queue import PriorityQueue

_PENTAGONAL_NUMS = [int(i*(i*3 -1)/2) for i in range(0, 10000000)]
_PN_LOOKUP = set(_PENTAGONAL_NUMS)

def pentagonal_dif(n, k):
    return abs(_PENTAGONAL_NUMS[n] - _PENTAGONAL_NUMS[n+k])

def pentagonal_add(n, k):
    return abs(_PENTAGONAL_NUMS[n] + _PENTAGONAL_NUMS[n+k])

def pentagonal_difs():
    _PN_DIFS = PriorityQueue()
    _PN_DIFS.put((4,1,1))
    highest_n = 2
    highest_n_dif = (3*(highest_n) + 1, highest_n, 1)
    _PN_DIFS.put(highest_n_dif)
    while True:
        min_dif = _PN_DIFS.get()
        _, n, k = min_dif
        _PN_DIFS.put((pentagonal_dif(n, k+1), n, k+1))
        if n == highest_n:
            highest_n += 1
            highest_n_dif = (3*(highest_n) + 1, highest_n, 1)
            _PN_DIFS.put(highest_n_dif)
        yield min_dif

def solution() -> int:
    for dif, n, k in pentagonal_difs():
        add = pentagonal_add(n, k)
        if add in _PN_LOOKUP and dif in _PN_LOOKUP:
            return dif


cpu_s, wall_s = time.process_time(), time.time()
result = solution()
cpu_e, wall_e = time.process_time(), time.time()

cpu_time, wall_time = cpu_e - cpu_s, wall_e - wall_s
print(json.dumps({"solution": result, "cpu": cpu_time, "wall": wall_time}))
