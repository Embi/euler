import json
import time

# START - CODE GENERATED BY gpt4
def solution():
    size = 1001
    total_sum = 1
    current_number = 1
    for layer in range(1, (size // 2) + 1):
        step = layer * 2
        for _ in range(4):
            current_number += step
            total_sum += current_number
    return total_sum
# END - CODE GENERATED BY gpt4

cpu_s, wall_s = time.process_time(), time.time()
result = solution()
cpu_e, wall_e = time.process_time(), time.time()

cpu_time, wall_time = cpu_e - cpu_s, wall_e - wall_s
print(json.dumps({"solution": result, "cpu": cpu_time, "wall": wall_time}))
