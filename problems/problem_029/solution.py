import json
import time
from typing import Dict, Tuple

def generate_combinations(a_len: int, b_len: int) -> Dict[int, Tuple[int, int]]:
    generated: Dict[int, Tuple[int, int]] = {}
    for a in range(2, a_len):
        for b in range(2, b_len):
            comb = (a,b)
            if a in generated:
                comb = (generated[a][0], generated[a][1] * b)
            if comb in generated.values():
                continue
            generated[comb[0]**comb[1]] = comb
    return generated

def solution() -> int:
    return len(generate_combinations(101,101))

cpu_s, wall_s = time.process_time(), time.time()
result = solution()
cpu_e, wall_e = time.process_time(), time.time()

cpu_time, wall_time = cpu_e - cpu_s, wall_e - wall_s
print(json.dumps({"solution": result, "cpu": cpu_time, "wall": wall_time}))
