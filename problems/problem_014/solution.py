import json
import time

_results = {}

def _collatz_sequence(n):
    if n in _results:
        return _results[n]

    collatz_sequence = [n]
    if n == 1:
        return collatz_sequence

    if n%2 == 0:
        collatz_sequence.extend(_collatz_sequence(n//2))
    else:
        collatz_sequence.extend(_collatz_sequence(3*n +1))

    _results[n] = collatz_sequence

    return collatz_sequence


def solution() -> int:
    max_len = 0
    max_starting_number = 0
    for i in range(1, 1000000):
        collatz_sequence = _collatz_sequence(i)
        if len(collatz_sequence) > max_len:
            max_len = len(collatz_sequence)
            max_starting_number = i
    return max_starting_number

cpu_s, wall_s = time.process_time(), time.time()
result = solution()
cpu_e, wall_e = time.process_time(), time.time()

cpu_time, wall_time = cpu_e - cpu_s, wall_e - wall_s
print(json.dumps({"solution": result, "cpu": cpu_time, "wall": wall_time}))
