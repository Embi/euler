import json
import time

# START - CODE GENERATED BY GPT
def solution():
    max_sum = 0
    for a in range(1, 100):
        for b in range(1, 100):
            num = a ** b
            digit_sum = sum(int(digit) for digit in str(num))
            if digit_sum > max_sum:
                max_sum = digit_sum
    return max_sum
# END - CODE GENERATED BY GPT

cpu_s, wall_s = time.process_time(), time.time()
result = solution()
cpu_e, wall_e = time.process_time(), time.time()

cpu_time, wall_time = cpu_e - cpu_s, wall_e - wall_s
print(json.dumps({"solution": result, "cpu": cpu_time, "wall": wall_time}))