import json
import time
from typing import Iterator

def four_digit_primes() -> Iterator[int]:
    for i in range(1000, 10000):
        is_prime = True
        for j in range(2, int(i**0.5)+1):
            if i%j == 0:
                is_prime = False
                break
        if is_prime:
            yield i

_PRIMES = set(four_digit_primes())

def prime_permutations(chars: str, perm: str='') -> Iterator[int]:
    if len(chars) == 0:
        perm = int(perm)
        if perm in _PRIMES:
            yield perm
    for i, ch in enumerate(chars):
        yield from prime_permutations(chars[:i] + chars[i+1:], perm+ch)


def solution() -> int:
    for prime in _PRIMES:
        perms = sorted(set(prime_permutations(str(prime))))
        for i in range(len(perms)):
            distances = set()
            for j in range(i+1, len(perms)):
                distance = perms[j] - perms[i]
                distances.add(distance)
                half_distance = distance/2
                if half_distance.is_integer():
                    half_distance = int(half_distance)
                    if half_distance in distances:
                        concat = str(perms[i])
                        concat += str(perms[i] + half_distance)
                        concat += str(perms[j])
                        return int(concat)

cpu_s, wall_s = time.process_time(), time.time()
result = solution()
cpu_e, wall_e = time.process_time(), time.time()

cpu_time, wall_time = cpu_e - cpu_s, wall_e - wall_s
print(json.dumps({"solution": result, "cpu": cpu_time, "wall": wall_time}))
