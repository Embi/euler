import json
import time


_PRIME_FACTORS = [set(), set()]
def solution() -> int:
    for n in range(2, 1000000):
        limit = int(n**0.5)+1
        prime_factors = set()
        for i in range(2, limit+1):
            if n % i == 0:
                prime_factors.add(i)
                prime_factors.update(_PRIME_FACTORS[n//i])
                break
        if not prime_factors:
            prime_factors.add(n)
        _PRIME_FACTORS.append(prime_factors)
        if all(map(lambda x: len(x) == 4, _PRIME_FACTORS[n-3:])):
            return n-3

cpu_s, wall_s = time.process_time(), time.time()
result = solution()
cpu_e, wall_e = time.process_time(), time.time()

cpu_time, wall_time = cpu_e - cpu_s, wall_e - wall_s
print(json.dumps({"solution": result, "cpu": cpu_time, "wall": wall_time}))
