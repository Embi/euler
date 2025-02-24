import json
import time

# START - CODE GENERATED BY GPT
from sympy import isprime

def solution():
    for i in range(11, 1000, 2):
        if not isprime(i):
            continue
        s = str(i)
        for j in range(len(s)):
            for k in range(j+1, len(s)):
                count = 0
                for d in range(10):
                    t = int(s[:j] + str(d) + s[j+1:k] + str(d) + s[k+1:])
                    if t > i and isprime(t):
                        count += 1
                if count == 7:
                    return i
    return None
# END - CODE GENERATED BY GPT

cpu_s, wall_s = time.process_time(), time.time()
result = solution()
cpu_e, wall_e = time.process_time(), time.time()

cpu_time, wall_time = cpu_e - cpu_s, wall_e - wall_s
print(json.dumps({"solution": result, "cpu": cpu_time, "wall": wall_time}))
