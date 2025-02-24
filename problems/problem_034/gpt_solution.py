import json
import time

# START - CODE GENERATED BY GPT
import math

def solution():
    total_sum = 0
    for i in range(3, 100000):
        digit_sum = 0
        for digit in str(i):
            digit_sum += math.factorial(int(digit))
        if digit_sum == i:
            total_sum += i
    return total_sum
# END - CODE GENERATED BY GPT

cpu_s, wall_s = time.process_time(), time.time()
result = solution()
cpu_e, wall_e = time.process_time(), time.time()

cpu_time, wall_time = cpu_e - cpu_s, wall_e - wall_s
print(json.dumps({"solution": result, "cpu": cpu_time, "wall": wall_time}))
