import json
import time

# START - CODE GENERATED BY gpt3
def solution():
    with open('p022_names.txt') as f:
        names = sorted(f.read().replace('"', '').split(','))
    total_score = 0
    for i, name in enumerate(names):
        score = sum(ord(c) - 64 for c in name)
        total_score += score * (i+1)
    return total_score
# END - CODE GENERATED BY gpt3

cpu_s, wall_s = time.process_time(), time.time()
result = solution()
cpu_e, wall_e = time.process_time(), time.time()

cpu_time, wall_time = cpu_e - cpu_s, wall_e - wall_s
print(json.dumps({"solution": result, "cpu": cpu_time, "wall": wall_time}))
