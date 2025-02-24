import json
import time
from typing import List, Iterable
import numpy as np

numbers = np.array([1, 2, 3, 4, 5, 6, 7, 8, 9])

def combinations(nums, length, comb=""):
    if length == 0:
        yield comb
    else:
        for idx, num in enumerate(nums):
            yield from combinations(
                nums[:idx] + nums[idx+1:], length - 1, comb + str(num))

def pandigital_1_to_9():
    for comb in combinations([1,2,3,4,5,6,7,8,9], 5):
        for i in [1,2]:
            multiplicand = comb[:i]
            multiplier = comb[i:5]
            product = int(multiplicand) * int(multiplier)
            identity = multiplier + multiplicand + str(product)
            if len(set(identity)) == len(identity) == 9 and '0' not in identity:
                yield product

def solution() -> int:
    return sum(set(pandigital_1_to_9()))

cpu_s, wall_s = time.process_time(), time.time()
result = solution()
cpu_e, wall_e = time.process_time(), time.time()

cpu_time, wall_time = cpu_e - cpu_s, wall_e - wall_s
print(json.dumps({"solution": result, "cpu": cpu_time, "wall": wall_time}))
