import json
import time

# START - CODE GENERATED BY GPT
def solution():
    num = 600851475143
    i = 2
    while i * i <= num:
        if num % i:
            i += 1
        else:
            num //= i
    return num
# END - CODE GENERATED BY GPT

cpu_s, wall_s = time.process_time(), time.time()
result = solution()
cpu_e, wall_e = time.process_time(), time.time()

cpu_time, wall_time = cpu_e - cpu_s, wall_e - wall_s
print(json.dumps({"solution": result, "cpu": cpu_time, "wall": wall_time}))