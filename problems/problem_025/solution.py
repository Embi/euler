import json
import time

def fibonacci():
    f_n_1, f_n_2 = (1,1)
    idx = 2
    while True:
        f_n_3 = f_n_1 + f_n_2
        f_n_1, f_n_2 = f_n_2, f_n_3
        idx += 1
        yield idx, f_n_3

def solution() -> int:
    for idx, fib in fibonacci():
        if len(str(fib)) >= 1000:
            return idx

cpu_s, wall_s = time.process_time(), time.time()
result = solution()
cpu_e, wall_e = time.process_time(), time.time()

cpu_time, wall_time = cpu_e - cpu_s, wall_e - wall_s
print(json.dumps({"solution": result, "cpu": cpu_time, "wall": wall_time}))
