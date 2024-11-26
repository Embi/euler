import json
import time
import numpy as np
from functools import lru_cache
from typing import List
from multiprocessing import Pool

def get_primes(up_to: int) -> List[int]:
    primes = list(range(up_to + 1))
    primes[0], primes[1] = 0, 0
    for i in primes:
        if not i:
            continue
        for j in range(2, up_to//i + 1):
            primes[i*j] = 0
    primes = list(set(primes))
    primes.remove(0)
    return sorted(primes)

_PRIMES = get_primes(1000000)
_PRIMES_LOOKUP = set(_PRIMES)

def get_prime_factors(n):
    prime_factors = set()
    limit = int(n**0.5) + 1
    for prime in _PRIMES:
        if prime == max(prime, min(limit, n)):
            break
        while n%prime == 0:
            prime_factors.add(prime)
            n = n // prime
    if n in _PRIMES_LOOKUP:
        prime_factors.add(n)
    return prime_factors

def get_totient(n):
    factors = get_prime_factors(n)
    non_relative_primes = set()
    for factor in factors:
        non_relative_primes.update(range(factor, n, factor))
    return (n - len(non_relative_primes) - 1)

def solution() -> int:
    x = []
    max_t = 0
    max_t_n = 0
    i = 2
    with Pool(10) as p:
        totients = list(p.imap(get_totient, range(200000, 300000), 10000))
        for totient in totients:
            max_t, max_t_n = max((max_t, max_t_n), (i/totient, i))
            i += 1
    return max_t_n

cpu_s, wall_s = time.process_time(), time.time()
result = solution()
cpu_e, wall_e = time.process_time(), time.time()

cpu_time, wall_time = cpu_e - cpu_s, wall_e - wall_s
print(json.dumps({"solution": result, "cpu": cpu_time, "wall": wall_time}))
