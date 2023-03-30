import json
import time

def is_prime(n):
    if n < 2:
        return False
    for i in range(2, int(n**0.5)+1):
        if n % i == 0:
            return False
    return True

def is_truncatable(n: str):
    for i in range(len(n)):
        if not all([is_prime(int(n[i:])), is_prime(int(n[:i+1]))]):
            return False
    return True

def solution() -> int:
    count, i, _sum = 0, 11, 0
    while count != 11:
        if is_truncatable(str(i)):
            _sum += i
            count += 1
        i+=1
    return _sum

cpu_s, wall_s = time.process_time(), time.time()
result = solution()
cpu_e, wall_e = time.process_time(), time.time()

cpu_time, wall_time = cpu_e - cpu_s, wall_e - wall_s
print(json.dumps({"solution": result, "cpu": cpu_time, "wall": wall_time}))
