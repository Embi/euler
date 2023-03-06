import json
import time

def factorial(n):
    _factorial = 1
    for i in range(n, 0, -1):
        _factorial *= i
    return _factorial


def digit_factorials(n):
    for i in range(n):
        if i in [1, 2]:
            continue
        digit_facts = sum(map(lambda x: factorial(int(x)), str(i)))
        if digit_facts == i:
            yield i

# no number above 2540160 (fac(9)*7) can be equal to sum of factorials of its digis
# since it is seven digit and it is the highest possible seven digit number we
# are able to get as sum of single digit factorials (9999999).
def solution() -> int:
    return sum(digit_factorials(2540160))

cpu_s, wall_s = time.process_time(), time.time()
result = solution()
cpu_e, wall_e = time.process_time(), time.time()

cpu_time, wall_time = cpu_e - cpu_s, wall_e - wall_s
print(json.dumps({"solution": result, "cpu": cpu_time, "wall": wall_time}))
