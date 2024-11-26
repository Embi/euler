import json
import time

def solution() -> int:
    with open('p067_triangle.txt', 'r') as f:
        content = f.read().strip()
        rows = content.split('\n')
        rows = [[int(num) for num in row.split(' ')] for row in rows]

    previous_max_paths = rows.pop()
    while len(rows) > 0:
        max_paths = rows.pop()
        for idx in range(len(max_paths)):
            max_paths[idx] = max_paths[idx] + max(
                previous_max_paths[idx],
                previous_max_paths[idx+1]
            )
        previous_max_paths = max_paths
    return previous_max_paths[0]


cpu_s, wall_s = time.process_time(), time.time()
result = solution()
cpu_e, wall_e = time.process_time(), time.time()

cpu_time, wall_time = cpu_e - cpu_s, wall_e - wall_s
print(json.dumps({"solution": result, "cpu": cpu_time, "wall": wall_time}))
