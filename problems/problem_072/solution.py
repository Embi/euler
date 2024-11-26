import json
import time
import math

def get_prime_factors(n: int):
    prime_factors = []
    i, j = 2, math.ceil(n**0.5)
    while i <= j:
        if n % i == 0:
            while n % i == 0:
                n //= i
            prime_factors.append(i)
        i += 1
        j = math.ceil(n**0.5)
    if n > 1:
        prime_factors.append(n)
    return prime_factors

def phi(n: int) -> int:
    """Calculate totient number"""
    tot = n
    prime_fac = get_prime_factors(n)
    for p in prime_fac:
        tot *= 1 - 1/p
    return int(tot)

def solution() -> int:
    d = 10**6
    total_elements = 0
    for i in range(2, d+1):
        total_elements += phi(i)
    return total_elements


cpu_s, wall_s = time.process_time(), time.time()
result = solution()
cpu_e, wall_e = time.process_time(), time.time()

cpu_time, wall_time = cpu_e - cpu_s, wall_e - wall_s
print(json.dumps({"solution": result, "cpu": cpu_time, "wall": wall_time}))
