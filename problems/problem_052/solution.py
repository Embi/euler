import json
import time
from itertools import count

def solution() -> int:
    for i in count(10):
        num_str = str(i)
        if int(num_str[0]) > 1 or int(num_str[1]) > 6:
            continue
        digits = sorted(num_str)
        for j in [2,3,4,5,6]:
            if digits != sorted(str(i*j)):
               break
        else:
            return i

cpu_s, wall_s = time.process_time(), time.time()
result = solution()
cpu_e, wall_e = time.process_time(), time.time()

cpu_time, wall_time = cpu_e - cpu_s, wall_e - wall_s
print(json.dumps({"solution": result, "cpu": cpu_time, "wall": wall_time}))
