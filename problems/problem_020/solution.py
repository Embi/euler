import json
import time

def factorial(n):
    _factorial = 1
    for i in range(n, 0, -1):
        _factorial *= i
    return _factorial

def digit_sum(n):
    digits = map(lambda x: int(x), str(n))
    return sum(digits)


def solution() -> int:
    return digit_sum(factorial(100))


cpu_s, wall_s = time.process_time(), time.time()
result = solution()
cpu_e, wall_e = time.process_time(), time.time()

cpu_time, wall_time = cpu_e - cpu_s, wall_e - wall_s
print(json.dumps({"solution": result, "cpu": cpu_time, "wall": wall_time}))
