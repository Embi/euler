import json
import time
from itertools import count

def get_period_length(num):
    continuation_lookup = {}
    a_0 = int(num**0.5)
    a_i, d_i, n_i = a_0, 1, a_0
    for i in count(1):
        d_i_1 = int((num - n_i**2) / d_i)
        if d_i_1 == 0:
            return 0
        a_i_1 = int((a_0 + n_i) / d_i_1)
        n_i_1 = abs(n_i - d_i_1*a_i_1)
        continuation = (a_i_1, d_i_1, n_i_1)
        if continuation in continuation_lookup:
            return i - continuation_lookup[continuation]
        continuation_lookup[continuation] = i
        a_i, d_i, n_i = a_i_1, d_i_1, n_i_1

def solution() -> int:
    return sum(get_period_length(i) % 2 == 1 for i in range(10000))

cpu_s, wall_s = time.process_time(), time.time()
result = solution()
cpu_e, wall_e = time.process_time(), time.time()

cpu_time, wall_time = cpu_e - cpu_s, wall_e - wall_s
print(json.dumps({"solution": result, "cpu": cpu_time, "wall": wall_time}))
