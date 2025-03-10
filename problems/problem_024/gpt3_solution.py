import json
import time

# START - CODE GENERATED BY gpt3
from math import factorial

def solution():
    digits = list(range(10))
    n = 1000000
    result = ''
    while len(digits) > 0:
        fact = factorial(len(digits)-1)
        index = (n-1) // fact
        result += str(digits[index])
        digits.pop(index)
        n -= index * fact
    return int(result)
# END - CODE GENERATED BY gpt3

cpu_s, wall_s = time.process_time(), time.time()
result = solution()
cpu_e, wall_e = time.process_time(), time.time()

cpu_time, wall_time = cpu_e - cpu_s, wall_e - wall_s
print(json.dumps({"solution": result, "cpu": cpu_time, "wall": wall_time}))