import json
import time

# START - CODE GENERATED BY gpt3
from itertools import permutations

def solution():
    max_string = 0
    for p in permutations(range(1, 11)):
        if p[0] > 5 or p[5] > 5:
            continue
        total = p[0] + p[5] + p[6]
        if sum(p[i] + p[i+5] + p[(i+6)%10] for i in range(5)) == total * 5:
            string = ''.join(str(p[i]) + str(p[i+5]) + str(p[(i+6)%10]) for i in range(5))
            if len(string) == 16 and int(string) > max_string:
                max_string = int(string)
    return max_string

# END - CODE GENERATED BY gpt3

cpu_s, wall_s = time.process_time(), time.time()
result = solution()
cpu_e, wall_e = time.process_time(), time.time()

cpu_time, wall_time = cpu_e - cpu_s, wall_e - wall_s
print(json.dumps({"solution": result, "cpu": cpu_time, "wall": wall_time}))
