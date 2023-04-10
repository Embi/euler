import json
import time
from itertools import groupby, combinations
from typing import List, Tuple, Iterable

def get_primes(up_to: int) -> List[int]:
    candidates = list(range(up_to))
    limit = int(up_to**0.5)+1
    for i in candidates:
        if i in [0,1]:
            continue
        if i == limit:
            break
        for j in range(i*2, up_to, i):
            candidates[j] = 0
    candidates = set(candidates)
    candidates.remove(0)
    candidates.remove(1)
    return sorted(candidates)

def sort_primes_per_order(primes: List[int]):
    primes_per_order = {}
    for prime in primes:
        order = len(str(prime))


def masks(digits: int) -> Iterable[Tuple[int]]:
    for i in range(digits):
        yield from combinations(range(digits), i+1)

def mask_out(number: int, mask: List[int], masked_value:str = ""):
    if len(mask) == 0:
        return number
    number = str(number)
    masked = ""
    for idx, digit in enumerate(number):
        if idx in mask:
            masked += masked_value
        else:
            masked += number[idx]
    return int(masked)

def is_mask_equal(number: int, mask: List[int]):
    """ Check if the masked digits are all equal
    """
    if len(mask) ==  1:
        return True
    number = str(number)
    masked_digit = None
    for idx, digit in enumerate(number):
        if idx in mask:
            if masked_digit is None:
                masked_digit = number[idx]
            if number[idx] != masked_digit:
                return False
    return True

def solution() -> int:
    _PRIMES = get_primes(1_000_000)
    _PRIMES_GROUPS = groupby(_PRIMES, lambda x: len(str(x)))
    _PRIMES_LOOKUP = set(_PRIMES)
    order_mask_groups = {}
    for order, primes in _PRIMES_GROUPS:
        primes = list(primes)
        for mask in masks(order-1):
            order_mask_groups[(order, mask)] = []
            for prime in primes:
                if is_mask_equal(prime, mask):
                    masked_prime = mask_out(prime, mask)
                    key = (order, masked_prime, mask)
                    order_mask_groups[key] = order_mask_groups.get(key, 0) + 1
                    if order_mask_groups[key] == 8:
                        for i in range(10):
                            candidate = mask_out(prime, mask, str(i))
                            if candidate in _PRIMES_LOOKUP:
                                return candidate

cpu_s, wall_s = time.process_time(), time.time()
result = solution()
cpu_e, wall_e = time.process_time(), time.time()

cpu_time, wall_time = cpu_e - cpu_s, wall_e - wall_s
print(json.dumps({"solution": result, "cpu": cpu_time, "wall": wall_time}))
