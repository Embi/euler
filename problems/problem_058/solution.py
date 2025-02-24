import json
import time
from typing import List, Iterator, Tuple

def is_prime(num: int) -> bool:
    for i in range(2, int(num**0.5)+1):
        if num % i == 0:
            return False
    return True

def spiral() -> Iterator[Tuple[int, int]]:
    i = 1
    spiral_num = 1
    while True:
        side = 1 + i*2
        for _ in [1,2,3,4]:
            spiral_num += 2*i
            yield spiral_num, side
        i+=1

def solution() -> int:
    spiral_prime_count = 0
    spiral_num_count = 1
    for num, side in spiral():
        spiral_num_count += 1
        if not (spiral_num_count % 4 == 1) and is_prime(num):
            spiral_prime_count += 1
        ratio = spiral_prime_count / spiral_num_count
        if ratio < 0.1:
            return side

cpu_s, wall_s = time.process_time(), time.time()
result = solution()
cpu_e, wall_e = time.process_time(), time.time()

cpu_time, wall_time = cpu_e - cpu_s, wall_e - wall_s
print(json.dumps({"solution": result, "cpu": cpu_time, "wall": wall_time}))
