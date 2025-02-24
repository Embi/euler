import json
import time
import math

def search_primes(up_to: int):
    primes = [2,3,5,7,11,13]
    for i in range(14, up_to):
        is_prime = True
        upper_bound = math.sqrt(i)
        for prime in primes:
            if prime > upper_bound:
                break
            if (i % prime) == 0:
                is_prime = False
                break
        if is_prime == True:
            primes.append(i)
    return primes

def solution() -> int:
    primes = search_primes(2000000)
    return sum(primes)

cpu_s, wall_s = time.process_time(), time.time()
result = solution()
cpu_e, wall_e = time.process_time(), time.time()

cpu_time, wall_time = cpu_e - cpu_s, wall_e - wall_s
print(json.dumps({"solution": result, "cpu": cpu_time, "wall": wall_time}))
