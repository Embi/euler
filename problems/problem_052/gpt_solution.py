import json
import time

# START - CODE GENERATED BY GPT
def solution():
    i = 1
    while True:
        if sorted(str(i)) == sorted(str(2*i)) == sorted(str(3*i)) == sorted(str(4*i)) == sorted(str(5*i)) == sorted(str(6*i)):
            return i
        i += 1
# END - CODE GENERATED BY GPT

cpu_s, wall_s = time.process_time(), time.time()
result = solution()
cpu_e, wall_e = time.process_time(), time.time()

cpu_time, wall_time = cpu_e - cpu_s, wall_e - wall_s
print(json.dumps({"solution": result, "cpu": cpu_time, "wall": wall_time}))