import json
import time

def solution() -> int:
    mul_3 = [3*i for i in range(1000//3+1)]
    mul_5 = [5*i for i in range(1000//5)]
    return sum(set(mul_3 + mul_5))

cpu_s, wall_s = time.process_time(), time.time()
result = solution()
cpu_e, wall_e = time.process_time(), time.time()

cpu_time, wall_time = cpu_e - cpu_s, wall_e - wall_s
print(json.dumps({"solution": result, "cpu": cpu_time, "wall": wall_time}))
