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

def solution() -> int:
    amicible_numbers = set()
    for i in range(10000):
        if i in amicible_numbers:
            continue
        i_pair = sum(proper_divisors(i))
        if sum(proper_divisors(i_pair)) == i:
            if i != i_pair:
                amicible_numbers.update([i, i_pair])
    return sum(amicible_numbers)


cpu_s, wall_s = time.process_time(), time.time()
result = solution()
cpu_e, wall_e = time.process_time(), time.time()

cpu_time, wall_time = cpu_e - cpu_s, wall_e - wall_s
print(json.dumps({"solution": result, "cpu": cpu_time, "wall": wall_time}))
