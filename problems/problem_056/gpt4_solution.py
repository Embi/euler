import json
import time

# START - CODE GENERATED BY gpt4
def solution():
    max_digit_sum = 0
    for a in range(1, 100):
        for b in range(1, 100):
            number = a ** b
            digit_sum = sum(int(digit) for digit in str(number))
            if digit_sum > max_digit_sum:
                max_digit_sum = digit_sum
    return max_digit_sum
# END - CODE GENERATED BY gpt4

cpu_s, wall_s = time.process_time(), time.time()
result = solution()
cpu_e, wall_e = time.process_time(), time.time()

cpu_time, wall_time = cpu_e - cpu_s, wall_e - wall_s
print(json.dumps({"solution": result, "cpu": cpu_time, "wall": wall_time}))
