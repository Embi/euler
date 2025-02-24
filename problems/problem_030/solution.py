import json
import time

def solution() -> int:
    numbers = []
    for i in range(354294):
        x = sum(map( lambda x: int(x)**5, str(i)))
        if x == i:
            numbers.append(i)
    return sum(numbers) - 1

cpu_s, wall_s = time.process_time(), time.time()
result = solution()
cpu_e, wall_e = time.process_time(), time.time()

cpu_time, wall_time = cpu_e - cpu_s, wall_e - wall_s
print(json.dumps({"solution": result, "cpu": cpu_time, "wall": wall_time}))
