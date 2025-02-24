import json
import time

# START - CODE GENERATED BY gpt4
def is_prime(n):
    if n <= 1:
        return False
    if n <= 3:
        return True
    if n % 2 == 0 or n % 3 == 0:
        return False
    i = 5
    while i * i <= n:
        if n % i == 0 or n % (i + 2) == 0:
            return False
        i += 6
    return True

def can_be_written_as_sum(n):
    for i in range(1, int((n // 2) ** 0.5) + 1):
        if is_prime(n - 2 * i * i):
            return True
    return False

def solution():
    n = 9
    while True:
        if not is_prime(n) and n % 2 == 1:
            if not can_be_written_as_sum(n):
                return n
        n += 2
# END - CODE GENERATED BY gpt4

cpu_s, wall_s = time.process_time(), time.time()
result = solution()
cpu_e, wall_e = time.process_time(), time.time()

cpu_time, wall_time = cpu_e - cpu_s, wall_e - wall_s
print(json.dumps({"solution": result, "cpu": cpu_time, "wall": wall_time}))
