import json
import time
from typing import Iterator


def pandigital_0_9(number: str = "9876543210", perm: str = "") -> Iterator:
    num_len = len(number)
    if num_len == 0:
        yield perm
    for i in range(num_len):
        if num_len == 10 and number[i] == '0':
            continue
        yield from pandigital_0_9(number[:i] + number[i+1:], perm + number[i])

def div_property(n: str) -> bool:
    primes = [1,2,3,5,7,11,13,17]
    for idx, prime in enumerate(primes):
        if int(n[idx:idx+3]) % prime != 0:
            return False
    return True

def solution() -> int:
    return sum(map(lambda x: int(x), filter(div_property, pandigital_0_9())))

cpu_s, wall_s = time.process_time(), time.time()
result = solution()
cpu_e, wall_e = time.process_time(), time.time()

cpu_time, wall_time = cpu_e - cpu_s, wall_e - wall_s
print(json.dumps({"solution": result, "cpu": cpu_time, "wall": wall_time}))
