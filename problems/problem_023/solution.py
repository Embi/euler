import json
import time

def proper_divisors(n):
    divisors = set()
    divisor = 1
    division = n
    while divisor < division:
        if (n % divisor) == 0:
            division = n // divisor
            divisors.update([divisor, division])
        divisor += 1

    try:
        divisors.remove(n)
    except KeyError:
        pass

    return divisors

def is_abundant(n):
    return n < sum(proper_divisors(n))


def solution() -> int:
    abundan_numbers = list(filter(is_abundant, range(28123)))
    numbers = list(range(28123))
    for idx, i in enumerate(abundan_numbers):
        for j in abundan_numbers[idx:]:
            if (i + j) >= 28123:
                break
            try:
                numbers[i+j] = 0
            except ValueError:
                pass
    return sum(numbers)

cpu_s, wall_s = time.process_time(), time.time()
result = solution()
cpu_e, wall_e = time.process_time(), time.time()

cpu_time, wall_time = cpu_e - cpu_s, wall_e - wall_s
print(json.dumps({"solution": result, "cpu": cpu_time, "wall": wall_time}))
