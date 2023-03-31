import json
import time

def solution() -> int:
    max_solutions = 0
    max_solutions_p = 0
    for p in range(1, 1001):
        x = [(2*p*b-p**2)/(2*b-2*p) for b in range(1,p//2)]
        x = list(filter(lambda x: x.is_integer(), x))
        solutions = len(x) // 2
        if solutions > max_solutions:
            max_solutions = solutions
            max_solutions_p = p
    return max_solutions_p


cpu_s, wall_s = time.process_time(), time.time()
result = solution()
cpu_e, wall_e = time.process_time(), time.time()

cpu_time, wall_time = cpu_e - cpu_s, wall_e - wall_s
print(json.dumps({"solution": result, "cpu": cpu_time, "wall": wall_time}))
