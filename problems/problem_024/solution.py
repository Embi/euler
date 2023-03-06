import json
import time

def factorial(n):
    _factorial = 1
    for i in range(n, 0, -1):
        _factorial *= i
    return _factorial


def nth_lexico_perm(n: int, chars):
    """
    Find nth lexicographical permutation
    of given characters.
    """
    _chars = sorted(chars)
    nth_permutation = []
    while n > 0:
        # number of all permutations minus the
        # first character
        sub_perm_count = factorial(len(_chars)-1)
        next_char_idx = n // sub_perm_count
        n -= sub_perm_count * next_char_idx
        nth_permutation.append(_chars.pop(next_char_idx))
    return nth_permutation + _chars


def solution() -> int:
    perm = nth_lexico_perm(
        1000001, ['0','1','2','3','4','5','6','7','8','9'])
    return int(''.join(perm))


cpu_s, wall_s = time.process_time(), time.time()
result = solution()
cpu_e, wall_e = time.process_time(), time.time()

cpu_time, wall_time = cpu_e - cpu_s, wall_e - wall_s
print(json.dumps({"solution": result, "cpu": cpu_time, "wall": wall_time}))
