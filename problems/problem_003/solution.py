import json
import time
import math

def prime_factors(n):
    suspect_factor = 2
    upper_bound = int(math.sqrt(n))
    factors = set()
    while suspect_factor <= upper_bound:
        if n % suspect_factor == 0:
            factors.add(suspect_factor)
            n = n // suspect_factor
        else:
            suspect_factor += 1
    factors.add(n)
    return factors

def solution() -> int:
    return max(prime_factors(600851475143))

cpu_s, wall_s = time.process_time(), time.time()
result = solution()
cpu_e, wall_e = time.process_time(), time.time()

cpu_time, wall_time = cpu_e - cpu_s, wall_e - wall_s
print(json.dumps({"solution": result, "cpu": cpu_time, "wall": wall_time}))
