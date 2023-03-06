import json
import time

def solution() -> int:
    sum_squares = sum(i*i for i in range(1, 101))
    square_sum = sum(range(1, 101))**2
    return square_sum - sum_squares

cpu_s, wall_s = time.process_time(), time.time()
result = solution()
cpu_e, wall_e = time.process_time(), time.time()

cpu_time, wall_time = cpu_e - cpu_s, wall_e - wall_s
print(json.dumps({"solution": result, "cpu": cpu_time, "wall": wall_time}))
