import json
import time

# START - CODE GENERATED BY gpt4
def solution():
    distinct_terms = set()
    for a in range(2, 101):
        for b in range(2, 101):
            distinct_terms.add(a ** b)
    return len(distinct_terms)
# END - CODE GENERATED BY gpt4

cpu_s, wall_s = time.process_time(), time.time()
result = solution()
cpu_e, wall_e = time.process_time(), time.time()

cpu_time, wall_time = cpu_e - cpu_s, wall_e - wall_s
print(json.dumps({"solution": result, "cpu": cpu_time, "wall": wall_time}))
