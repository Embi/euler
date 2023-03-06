import json
import time
import math

def get_primes(n):
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
    numbers.remove(0)
    numbers.remove(-1)
    return list(numbers)

def rotations(number):
    rotation = str(number)
    for i in range(len(rotation)):
        rotation = rotation[1:] + rotation[:1]
        yield int(rotation)

def circular_primes(primes):
    _circular_primes = []
    primes = list(filter(lambda x: '0' not in str(x), primes))
    for prime in primes:
        _rotations = list(rotations(prime))
        try:
            for rotation in _rotations:
                primes.remove(rotation)
        except ValueError:
            continue
        _circular_primes.extend(_rotations)
    return _circular_primes


def solution() -> int:
    pass

cpu_s, wall_s = time.process_time(), time.time()
result = solution()
cpu_e, wall_e = time.process_time(), time.time()

cpu_time, wall_time = cpu_e - cpu_s, wall_e - wall_s
print(json.dumps({"solution": result, "cpu": cpu_time, "wall": wall_time}))
