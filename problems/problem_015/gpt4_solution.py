import json
import time

# START - CODE GENERATED BY gpt4
def solution():
    grid_size = 20
    paths = 1
    for i in range(1, grid_size + 1):
        paths = paths * (grid_size + i) // i
    return paths
# END - CODE GENERATED BY gpt4

cpu_s, wall_s = time.process_time(), time.time()
result = solution()
cpu_e, wall_e = time.process_time(), time.time()

cpu_time, wall_time = cpu_e - cpu_s, wall_e - wall_s
print(json.dumps({"solution": result, "cpu": cpu_time, "wall": wall_time}))
