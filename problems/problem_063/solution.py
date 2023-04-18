import json
import time
from itertools import count

def solution() -> int:
    powerful_digits = 0
    for i in [1,2,3,4,5,6,7,8,9]:
        for j in count(1):
            digits = str(i**j)
            if len(digits) == j:
                powerful_digits += 1
            elif len(digits) < j:
                break
    return powerful_digits

cpu_s, wall_s = time.process_time(), time.time()
result = solution()
cpu_e, wall_e = time.process_time(), time.time()

cpu_time, wall_time = cpu_e - cpu_s, wall_e - wall_s
print(json.dumps({"solution": result, "cpu": cpu_time, "wall": wall_time}))
