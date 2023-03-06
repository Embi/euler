import json
import time
import math
from itertools import count

def generate_triples():
    for b in count():
        b_squared = b*b
        for n in count():
            a_squared = b*n*2 + n*n
            if a_squared >= b_squared:
                break
            a = math.sqrt(a_squared)
            if (a % 1) == 0:
                yield a, b, b+n

def solution() -> int:
    for triplet in generate_triples():
        if sum(triplet) == 1000:
            a,b,c = triplet
            return int(a*b*c)

cpu_s, wall_s = time.process_time(), time.time()
result = solution()
cpu_e, wall_e = time.process_time(), time.time()

cpu_time, wall_time = cpu_e - cpu_s, wall_e - wall_s
print(json.dumps({"solution": result, "cpu": cpu_time, "wall": wall_time}))
