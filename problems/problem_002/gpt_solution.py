import json
import time

# START - SOLUTION GENERATE BY GPT
def solution():
    sum = 0
    a, b = 1, 2
    while b <= 4000000:
        if b % 2 == 0:
            sum += b
        a, b = b, a + b
    return sum
# END - SOLUTION GENERATE BY GPT

cpu_s, wall_s = time.process_time(), time.time()
result = solution()
cpu_e, wall_e = time.process_time(), time.time()

cpu_time, wall_time = cpu_e - cpu_s, wall_e - wall_s
print(json.dumps({"solution": result, "cpu": cpu_time, "wall": wall_time}))