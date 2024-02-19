import json
import time
from itertools import count
from typing import Iterator, Tuple

def gen_sqrt_continued_fraction(num: int) -> Iterator[Tuple[int, int]]:
    """Generate continued fraction for sqrt of num
    """
    a_0 = int(num**0.5)
    a_i, d_i, n_i = a_0, 1, a_0
    for i in count(1):
        d_i_1 = int((num - n_i**2) / d_i)
        if d_i_1 == 0:
            return 0
        a_i_1 = int((a_0 + n_i) / d_i_1)
        n_i_1 = abs(n_i - d_i_1*a_i_1)
        yield a_i
        a_i, d_i, n_i = a_i_1, d_i_1, n_i_1


def gen_convergents(num: int) -> Iterator[Tuple[int, int]]:
    """Generate convergents (numerator, denominator) that approximates
    sqrt of num
    """
    continued_fractions = []
    for frac in gen_sqrt_continued_fraction(num):
        continued_fractions.append(frac)
        n, d = 0, 1
        for i in reversed(continued_fractions):
            n, d = d, d*i + n
        yield n, d

def minimal_x_solution(D: int) -> int:
    """Get the minimal (in x) solution for the diophantine equation
    x^2 - Dy^2 = 1
    """
    # n-numerator d-denominator
    for n, d in gen_convergents(D):
        if d**2 - D*n**2 == 1:
            return d

def solution() -> int:
    largest_x = 0
    largest_d = 0
    for d in range(2, 1001):
        x = minimal_x_solution(d)
        if x is None:
            continue
        if x > largest_x:
            largest_x = x
            largest_d = d
    return largest_d


cpu_s, wall_s = time.process_time(), time.time()
result = solution()
cpu_e, wall_e = time.process_time(), time.time()

cpu_time, wall_time = cpu_e - cpu_s, wall_e - wall_s
print(json.dumps({"solution": result, "cpu": cpu_time, "wall": wall_time}))
