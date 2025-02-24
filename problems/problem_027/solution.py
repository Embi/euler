import json
import time
from itertools import count
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

primes = search_primes(1000)
possible_primes = set(search_primes(1000000))

def get_primes_seq_len(a, b):
    for i in count():
        candidate = i*i + a*i + b
        if candidate <= 0 or candidate not in possible_primes:
            return i

def solution() -> int:
    max_ab = None
    max_ab_len = 0
    for a in range(-999, 1000):
        for b in primes:
            seq_len = get_primes_seq_len(a, b)
            if seq_len > max_ab_len:
                max_ab = (a,b)
                max_ab_len = seq_len
    a, b = max_ab
    return a*b

cpu_s, wall_s = time.process_time(), time.time()
result = solution()
cpu_e, wall_e = time.process_time(), time.time()

cpu_time, wall_time = cpu_e - cpu_s, wall_e - wall_s
print(json.dumps({"solution": result, "cpu": cpu_time, "wall": wall_time}))
