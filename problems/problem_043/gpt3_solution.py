import json
import time

# START - CODE GENERATED BY gpt3
from itertools import permutations

def solution():
    primes = [2, 3, 5, 7, 11, 13, 17]
    total_sum = 0
    for perm in permutations('0123456789'):
        if perm[0] == '0':
            continue
        divisible = True
        for i in range(7):
            if int(''.join(perm[i+1:i+4])) % primes[i] != 0:
                divisible = False
                break
        if divisible:
            total_sum += int(''.join(perm))
    return total_sum
# END - CODE GENERATED BY gpt3

cpu_s, wall_s = time.process_time(), time.time()
result = solution()
cpu_e, wall_e = time.process_time(), time.time()

cpu_time, wall_time = cpu_e - cpu_s, wall_e - wall_s
print(json.dumps({"solution": result, "cpu": cpu_time, "wall": wall_time}))
