import json
import time
from queue import LifoQueue

def solution() -> int:
    lychrel = [-1]*10000
    stack = LifoQueue()
    for idx, is_lychrel in enumerate(lychrel):
        if is_lychrel in [1, 0]:
            continue
        assert stack.empty()
        stack.put(idx)
        iteration = idx
        while True:
            # Calc next interation
            iteration = iteration + int(str(iteration)[::-1])
            if stack.qsize() > 50:
                while not stack.empty():
                    num = stack.get()
                    if num < 10000:
                        lychrel[num] = 1
                break
            if str(iteration) == str(iteration)[::-1]:
                while not stack.empty():
                    num = stack.get()
                    if num < 10000:
                        lychrel[num] = 0
                break
            stack.put(iteration)
    return sum(lychrel)

cpu_s, wall_s = time.process_time(), time.time()
result = solution()
cpu_e, wall_e = time.process_time(), time.time()

cpu_time, wall_time = cpu_e - cpu_s, wall_e - wall_s
print(json.dumps({"solution": result, "cpu": cpu_time, "wall": wall_time}))
