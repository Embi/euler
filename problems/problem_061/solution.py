import json
import time
from typing import Callable, List
from itertools import count

def gen_4d_polygonal(formula: Callable[[int], int]) -> List[int]:
    """Generate 4 digit plygonal numbers based on formula (e.g. n*(n+1)/2)
    """
    for n in count(1):
        num = int(formula(n))
        if len(str(num)) == 4:
            yield num
        if len(str(num)) > 4:
            return

tria = {str(i)[:2]: str(i)[2:] for i in gen_4d_polygonal(lambda n: n*(n+1)/2)}
squa = {str(i)[:2]: str(i)[2:] for i in gen_4d_polygonal(lambda n: n*n)}
pent = {str(i)[:2]: str(i)[2:] for i in gen_4d_polygonal(lambda n: n*(3*n-1)/2)}
hexa = {str(i)[:2]: str(i)[2:] for i in gen_4d_polygonal(lambda n: n*(2*n-1))}
hept = {str(i)[:2]: str(i)[2:] for i in gen_4d_polygonal(lambda n: n*(5*n-3)/2)}
octa = {str(i)[:2]: str(i)[2:] for i in gen_4d_polygonal(lambda n: n*(3*n-2))}

def find_cycle(prefix, polygonals, start_prefix):
    if len(polygonals) == 0:
        if prefix == start_prefix:
            return []
        else:
            return None
    for idx, polygonal in enumerate(polygonals):
        if prefix in polygonal:
            cycle = find_cycle(
                prefix=polygonal[prefix],
                polygonals=polygonals[:idx]+polygonals[idx+1:],
                start_prefix=start_prefix
            )
            if cycle is not None:
                return cycle + [int(prefix + polygonal[prefix])]
    return None

def solution() -> int:
    for pre, suf in tria.items():
        cycle = find_cycle(suf, [squa, pent, hexa, hept, octa], pre)
        if cycle is not None:
            return sum(cycle + [int(pre + suf)])

cpu_s, wall_s = time.process_time(), time.time()
result = solution()
cpu_e, wall_e = time.process_time(), time.time()

cpu_time, wall_time = cpu_e - cpu_s, wall_e - wall_s
print(json.dumps({"solution": result, "cpu": cpu_time, "wall": wall_time}))
