import json
import time
from typing import List, Iterator
from functools import reduce


def perms(nums: List[int], perm_len: int, perm: List[int] = []) -> Iterator[List[int]]:
    if len(perm) == perm_len:
        yield perm
    for idx, num in enumerate(nums):
        yield from perms(nums[:idx] + nums[idx+1:], perm_len,
                         perm + [nums[idx]])

def find_magic_5_gons(line, lines_lookup, lines=[]):
    lines = lines + [line]
    if len(lines) == 5:
        if lines[0][1] == lines[-1][2]:
            yield lines
        return
    for next_line in lines_lookup[line[2]]:
        set_len = len(set(reduce(lambda x, y: x+y, lines + [next_line])))
        expected_set_len = 3 + 2*(len(lines)) - 1*((len(lines) + 1)//5)
        if next_line not in lines and set_len == expected_set_len:
            yield from find_magic_5_gons(next_line, lines_lookup, lines)


def solution() -> int:
    permutations = list(perms(list(range(1,11)), 3))
    magic_5_gons = []
    for i in range(10, 24):
        lines = list(filter(lambda line: sum(line) == i, permutations))
        lines_lookup = {i: [] for i in range(1,11)}
        for line in lines:
            lines_lookup[line[1]].append(line)
        for line in lines:
            for magic_5_gon in find_magic_5_gons(line, lines_lookup):
                magic_5_gons.append(magic_5_gon)

    max_16_digit_string = 0
    for magic_5_gon in  magic_5_gons:
        min_value, min_i = magic_5_gon[0][0], 0
        for idx, line in enumerate(magic_5_gon):
            min_value, min_i = min((min_value, min_i), (line[0], idx))
        magic_5_gon = magic_5_gon[min_i:] + magic_5_gon[:min_i]
        digits_str = ''.join([str(i) for i in reduce(lambda x, y: x+y,
                                                     magic_5_gon)])
        if len(digits_str) == 16:
            max_16_digit_string = max(max_16_digit_string, int(digits_str))
    return max_16_digit_string


cpu_s, wall_s = time.process_time(), time.time()
result = solution()
cpu_e, wall_e = time.process_time(), time.time()

cpu_time, wall_time = cpu_e - cpu_s, wall_e - wall_s
print(json.dumps({"solution": result, "cpu": cpu_time, "wall": wall_time}))
