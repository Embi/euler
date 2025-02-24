import json
import time

def solution() -> int:
    more_digit_numer = 0
    n, d = 3, 2
    for i in range(1000):
        n, d = n + 2*d, n + d
        if len(str(n)) > len(str(d)):
            more_digit_numer += 1
    return more_digit_numer

cpu_s, wall_s = time.process_time(), time.time()
result = solution()
cpu_e, wall_e = time.process_time(), time.time()

cpu_time, wall_time = cpu_e - cpu_s, wall_e - wall_s
print(json.dumps({"solution": result, "cpu": cpu_time, "wall": wall_time}))
