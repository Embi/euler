import json
import time

def solution() -> int:
    triangle = set(n*(n+1)//2 for n in range(1000000))
    pentagonal = set(n*(3*n-1)//2 for n in range(1000000))
    hexagonal = set(n*(2*n-1) for n in range(1000000))
    intersection = triangle.intersection(hexagonal).intersection(pentagonal)
    intersection = sorted(intersection)
    for i in intersection:
        if i > 40755:
            return i


cpu_s, wall_s = time.process_time(), time.time()
result = solution()
cpu_e, wall_e = time.process_time(), time.time()

cpu_time, wall_time = cpu_e - cpu_s, wall_e - wall_s
print(json.dumps({"solution": result, "cpu": cpu_time, "wall": wall_time}))
