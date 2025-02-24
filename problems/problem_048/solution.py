import json
import time

def solution() -> int:
    series = sum(map(lambda x: x**x, range(1, 1001)))
    return int(str(series)[-10:])

cpu_s, wall_s = time.process_time(), time.time()
result = solution()
cpu_e, wall_e = time.process_time(), time.time()

cpu_time, wall_time = cpu_e - cpu_s, wall_e - wall_s
print(json.dumps({"solution": result, "cpu": cpu_time, "wall": wall_time}))
