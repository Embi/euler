import json
import time
from itertools import count

def solution() -> int:
    cubes = {}
    for i in count(1):
        digits = str(''.join(sorted(str(i**3))))
        if digits not in cubes:
            cubes[digits] = []
        cubes[digits] += [i]
        if len(cubes[digits]) == 5:
            return min(cubes[digits])**3

cpu_s, wall_s = time.process_time(), time.time()
result = solution()
cpu_e, wall_e = time.process_time(), time.time()

cpu_time, wall_time = cpu_e - cpu_s, wall_e - wall_s
print(json.dumps({"solution": result, "cpu": cpu_time, "wall": wall_time}))
