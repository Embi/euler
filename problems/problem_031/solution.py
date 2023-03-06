from typing import Dict, List, Tuple
import numpy as np
import json
import time

coins = np.array([1, 2, 5, 10, 20, 50, 100, 200])

results: Dict[Tuple[int, int], int] = {}
def possible_changes(total: int, coins):
    if len(coins) == 0:
        return 0
    if (total, len(coins)) in results:
        return results[(total, len(coins))]
    changes = 0
    for coin in coins[-1::-1]:
        for i in range(total // coin):
            _total = total - coin*(i+1)
            if _total == 0:
                changes += 1
            else:
                changes += possible_changes(_total, coins[coins<coin])
    return changes

def solution() -> int:
    return possible_changes(200, coins)

cpu_s, wall_s = time.process_time(), time.time()
result = solution()
cpu_e, wall_e = time.process_time(), time.time()

cpu_time, wall_time = cpu_e - cpu_s, wall_e - wall_s
print(json.dumps({"solution": result, "cpu": cpu_time, "wall": wall_time}))
