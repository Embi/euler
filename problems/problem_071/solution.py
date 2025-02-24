import json
import time
import math

def solution() -> int:
    target = 3/7
    biggest = 0
    biggest_n, biggest_d = 0, 0
    for n in range(1, 10**6):
        d = math.ceil(n / target)
        # we only consider d <= 10**6
        if d > 10**6:
            break
        assert n/d <= target
        if n/d == target:
            continue
        if n/d > biggest:
            biggest = n/d
            biggest_n, biggest_d = (n, d)
    return biggest_n

cpu_s, wall_s = time.process_time(), time.time()
result = solution()
cpu_e, wall_e = time.process_time(), time.time()

cpu_time, wall_time = cpu_e - cpu_s, wall_e - wall_s
print(json.dumps({"solution": result, "cpu": cpu_time, "wall": wall_time}))
