import json
import time

def is_prime(n):
    for i in range(2, int(n**0.5)+1):
        if n%i == 0:
            return False
    return True

def combinations(n, chars:str, perm=''):
    if n == 0:
        yield perm
    else:
        for i in range(len(chars)):
            yield from combinations(
                n-1, chars[:i] + chars[i+1:], perm+chars[i])

def solution() -> int:
    for i in range(9, 3, -1):
        for pandigital in combinations(i, '987654321'[-i:], ''):
            if is_prime(int(pandigital)):
                return int(pandigital)

cpu_s, wall_s = time.process_time(), time.time()
result = solution()
cpu_e, wall_e = time.process_time(), time.time()

cpu_time, wall_time = cpu_e - cpu_s, wall_e - wall_s
print(json.dumps({"solution": result, "cpu": cpu_time, "wall": wall_time}))
