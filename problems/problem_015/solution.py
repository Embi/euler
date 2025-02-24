import json
import time
import numpy as np

def solution() -> int:
    grid = np.zeros((21,21), dtype=np.int64)

    grid[20,20] = 1
    for i in range(20, -1, -1):
        for j in range(20, -1, -1):
            try:
                grid[i,j] += grid[i, j+1]
            except IndexError:
                pass
            try:
                grid[i,j] += grid[i+1, j]
            except IndexError:
                pass

    return int(grid[0,0])

cpu_s, wall_s = time.process_time(), time.time()
result = solution()
cpu_e, wall_e = time.process_time(), time.time()

cpu_time, wall_time = cpu_e - cpu_s, wall_e - wall_s
print(json.dumps({"solution": result, "cpu": cpu_time, "wall": wall_time}))
