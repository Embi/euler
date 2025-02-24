import json
import time

def is_permutation(x: int, y: int) -> bool:
    x_s = str(x)
    y_s = str(y)
    if len(x_s) != len(y_s):
        return False
    return sorted(str(x)) == sorted(str(y))

def totient(n: int) -> int:
    rp = n # relatively prime numbers
    fac = 2
    while fac**2 <= n:
        if n % fac == 0:
            while n % fac == 0:
                n //= fac
            rp -= rp // fac
        fac += 1
    if n > 1:
        rp -= rp // n
    return rp

def solution() -> int:
    min_ratio = 10**7
    min_i = 1
    for i in range(2, 10**7):
        if 0 in [i % 2, i % 3, i % 5, i % 7]:
            continue
        tot = totient(i)
        if not is_permutation(i, tot):
            continue
        ratio = i / tot
        if min_ratio > ratio:
            min_ratio = ratio
            min_i = i
    return min_i

cpu_s, wall_s = time.process_time(), time.time()
result = solution()
cpu_e, wall_e = time.process_time(), time.time()

cpu_time, wall_time = cpu_e - cpu_s, wall_e - wall_s
print(json.dumps({"solution": result, "cpu": cpu_time, "wall": wall_time}))
