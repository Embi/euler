import json
import time

__HIGHEST_POSSIBLE = 998001

def is_palindrom(number):
    num_str = str(number)
    middle_idx = len(num_str)//2
    return num_str[:middle_idx] == num_str[::-1][:middle_idx]

def solution() -> int:
    for i in range(999,800,-1):
        for j in range(999,800,-1):
            num = i*j
            if is_palindrom(num):
                return num

cpu_s, wall_s = time.process_time(), time.time()
result = solution()
cpu_e, wall_e = time.process_time(), time.time()

cpu_time, wall_time = cpu_e - cpu_s, wall_e - wall_s
print(json.dumps({"solution": result, "cpu": cpu_time, "wall": wall_time}))
