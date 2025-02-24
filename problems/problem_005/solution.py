import json
import time
import math

def prime_decomposition(n):
    suspect_factor = 2
    upper_bound = int(math.sqrt(n)) + 1
    factors = {}
    while suspect_factor < upper_bound:
        if n % suspect_factor == 0:
            if suspect_factor not in factors:
                factors[suspect_factor] = 0
            factors[suspect_factor] += 1
            n = n // suspect_factor
        else:
            suspect_factor += 1
    if n not in factors:
        factors[n] = 0
    factors[n] += 1
    return factors

def smallest_multiple(n):
    factors = {}
    for i in range(1, n+1):
        for factor, count in prime_decomposition(i).items():
            if factor not in factors:
                factors[factor] = count
            elif factors[factor] < count:
                factors[factor] = count
    smallest_multiple = 1
    for factor, count in factors.items():
        smallest_multiple *= factor**count
    return smallest_multiple

def solution() -> int:
    return smallest_multiple(20)

cpu_s, wall_s = time.process_time(), time.time()
result = solution()
cpu_e, wall_e = time.process_time(), time.time()

cpu_time, wall_time = cpu_e - cpu_s, wall_e - wall_s
print(json.dumps({"solution": result, "cpu": cpu_time, "wall": wall_time}))
