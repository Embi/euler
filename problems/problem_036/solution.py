import json
import time
from typing import List

def is_palindrome(string: str) -> bool:
    middle_idx = len(string) // 2
    return string[:middle_idx] == string[-1: -(middle_idx+1): -1]

def double_base_palindromes(below: int) -> List[int]:
    _double_base_palindromes = []
    for base_10 in range(below):
        base_2 = bin(base_10).replace('0b', '')
        if all([is_palindrome(str(base_10)), is_palindrome(base_2)]):
            _double_base_palindromes.append(base_10)
    return _double_base_palindromes

def solution() -> int:
    return sum(double_base_palindromes(1000000))


cpu_s, wall_s = time.process_time(), time.time()
result = solution()
cpu_e, wall_e = time.process_time(), time.time()

cpu_time, wall_time = cpu_e - cpu_s, wall_e - wall_s
print(json.dumps({"solution": result, "cpu": cpu_time, "wall": wall_time}))
