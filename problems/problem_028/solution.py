import json
import time
from typing import Iterator

def diag_1(n: int) -> Iterator[int]:
    elem = 1
    for i in range(n):
        elem += i * 2
        yield elem

def diag_2(n: int) -> Iterator[int]:
    elem = 1
    for i in range(n):
        elem += (1+i//2) * 4
        yield elem

def solution() -> int:
    return sum(diag_1(1001)) + sum(diag_2(1000))

cpu_s, wall_s = time.process_time(), time.time()
result = solution()
cpu_e, wall_e = time.process_time(), time.time()

cpu_time, wall_time = cpu_e - cpu_s, wall_e - wall_s
print(json.dumps({"solution": result, "cpu": cpu_time, "wall": wall_time}))
