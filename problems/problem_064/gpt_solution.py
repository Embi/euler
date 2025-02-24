import json
import time

# START - CODE GENERATED BY GPT
def solution():
    def is_square(n):
        return int(n**0.5)**2 == n

    def continued_fraction(n):
        a0 = int(n**0.5)
        if is_square(n):
            return [a0]
        m, d, a = 0, 1, a0
        result = [a0]
        while a != 2*a0:
            m = d*a - m
            d = (n - m**2) // d
            a = (a0 + m) // d
            result.append(a)
        return result

    count = 0
    for n in range(2, 10001):
        if len(continued_fraction(n)) % 2 == 0:
            continue
        count += 1
    return count
# END - CODE GENERATED BY GPT

cpu_s, wall_s = time.process_time(), time.time()
result = solution()
cpu_e, wall_e = time.process_time(), time.time()

cpu_time, wall_time = cpu_e - cpu_s, wall_e - wall_s
print(json.dumps({"solution": result, "cpu": cpu_time, "wall": wall_time}))
