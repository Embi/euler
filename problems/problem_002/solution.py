import json
import time

def fibonnaci_even_sum(max_n):
    f_sum = 2
    n_2, n_1, n = 1, 2, 3
    while n < max_n:
        if n % 2 == 0:
            f_sum += n
        n_2, n_1, n = n_1, n, n_1 + n
    return f_sum

def solution() -> int:
    return fibonnaci_even_sum(4000000)

cpu_s, wall_s = time.process_time(), time.time()
result = solution()
cpu_e, wall_e = time.process_time(), time.time()

cpu_time, wall_time = cpu_e - cpu_s, wall_e - wall_s
print(json.dumps({"solution": result, "cpu": cpu_time, "wall": wall_time}))
