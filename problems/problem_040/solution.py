import json
import time
from itertools import count

def solution() -> int:
    target_counts = [1, 10, 100, 1000, 10000, 100000, 1000000]
    digit_count = 0
    digit_product = 1
    next_target_count = target_counts.pop(0)
    concat_str = ''
    for i in count(1):
        str_i = str(i)
        digit_count += len(str_i)
        if digit_count >= next_target_count:
            digit_product *= int(str_i[-(1 + digit_count % next_target_count)])
            if len(target_counts) == 0:
                return digit_product
            next_target_count = target_counts.pop(0)

cpu_s, wall_s = time.process_time(), time.time()
result = solution()
cpu_e, wall_e = time.process_time(), time.time()

cpu_time, wall_time = cpu_e - cpu_s, wall_e - wall_s
print(json.dumps({"solution": result, "cpu": cpu_time, "wall": wall_time}))
