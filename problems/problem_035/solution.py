import json
import time
import math
from typing import Set, Iterator

def get_primes(n: int) -> Set[int]:
    numbers = list(range(n))
    # Bound for primality check
    max_check = int(math.sqrt(n)) + 1
    idx = 2
    while numbers[idx] < max_check:
        for i in range(2, n//numbers[idx]+1):
            try:
                numbers[numbers[idx]*i] = -1
            except IndexError:
                pass
        idx += 1
    numbers = set(numbers)
    numbers.remove(-1)
    numbers.remove(0)
    numbers.remove(1)
    return numbers

def rotations(number: int) -> Iterator[int]:
    rotation = str(number)
    for i in range(len(rotation)):
        rotation = rotation[1:] + rotation[:1]
        yield int(rotation)

def circular_primes(below_n: int) -> Set[int]:
    _circular_primes = set()
    primes = get_primes(below_n)
    # A prime that contains 0 can not be circular because at lease one rotation
    # will be evenly divisible by 10
    primes = set(filter(lambda x: '0' not in str(x), primes))
    for prime in primes:
        if prime in _circular_primes:
            continue
        _rotations = list(rotations(prime))
        try:
            for rotation in _rotations:
                assert rotation in primes
        except AssertionError:
            continue
        _circular_primes.update(_rotations)
    return _circular_primes


def solution() -> int:
    return len(circular_primes(1000000))

cpu_s, wall_s = time.process_time(), time.time()
result = solution()
cpu_e, wall_e = time.process_time(), time.time()

cpu_time, wall_time = cpu_e - cpu_s, wall_e - wall_s
print(json.dumps({"solution": result, "cpu": cpu_time, "wall": wall_time}))
