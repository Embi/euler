import json
import time
from functools import reduce

def highest_common_denom(a, b):
    a, b = sorted((a,b))
    while a != b:
        a, b = sorted((b-a,a))
    return a

def simplify(n, d):
    """simplify fraction given by numerator n and denominator d
    """
    common_d = highest_common_denom(n, d)
    return(n//common_d, d//common_d)


def curious_fractions():
    for i in range(1, 10):
        for j in range(1, i):
            for k in range(1, 10):
                n = 10*j + i
                d = 10*i + k
                if simplify(n,d) == simplify(j, k):
                    yield simplify(n, d)

def solution() -> int:
    fractions = list(curious_fractions())
    product = reduce(lambda x, y: (x[0]*y[0], x[1]*y[1]), fractions)
    num, denom = simplify(*product)
    return denom

cpu_s, wall_s = time.process_time(), time.time()
result = solution()
cpu_e, wall_e = time.process_time(), time.time()

cpu_time, wall_time = cpu_e - cpu_s, wall_e - wall_s
print(json.dumps({"solution": result, "cpu": cpu_time, "wall": wall_time}))
