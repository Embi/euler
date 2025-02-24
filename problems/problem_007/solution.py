import json
import time
import math

def search_primes(up_to: int):
    primes = [2,3,5,7,11,13]
    for i in range(14, up_to):
        is_prime = True
        prime_bound = int(math.sqrt(i))
        for prime in primes:
            if prime > prime_bound:
                break
            if (i % prime) == 0:
                is_prime = False
                break
        if is_prime == True:
            primes.append(i)
    return primes

def solution() -> int:
    x = search_primes(120000)
    return x[10000]

cpu_s, wall_s = time.process_time(), time.time()
result = solution()
cpu_e, wall_e = time.process_time(), time.time()

cpu_time, wall_time = cpu_e - cpu_s, wall_e - wall_s
print(json.dumps({"solution": result, "cpu": cpu_time, "wall": wall_time}))
