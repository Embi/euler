import json
import time
from typing import Set
from itertools import count

_LONGEST_ENGLISH_WORD = "pneumonoultramicroscopicsilicovolcanoconiosis".upper()
_SCORE = {char: idx+1 for idx, char in
          enumerate("ABCDEFGHIJKLMNOPQRSTUVWXYZ")}

def triangle_numbers(below: int) -> Set[int]:
    # Use set for fast O(1) lookup
    triang_nums = set()
    for n in count(1):
        triang_num = int(n*(n+1)/2)
        if triang_num > below:
            return triang_nums
        triang_nums.add(triang_num)

def score(word: str) -> int:
    return sum(map(lambda x: _SCORE[x], word))

def solution() -> int:
    triang_nums = triangle_numbers(score(_LONGEST_ENGLISH_WORD))
    with open('p042_words.txt', 'r') as f:
        words = f.read().replace('"', '').split(',')
    return len(list(filter(lambda x: score(x) in triang_nums, words)))

cpu_s, wall_s = time.process_time(), time.time()
result = solution()
cpu_e, wall_e = time.process_time(), time.time()

cpu_time, wall_time = cpu_e - cpu_s, wall_e - wall_s
print(json.dumps({"solution": result, "cpu": cpu_time, "wall": wall_time}))
