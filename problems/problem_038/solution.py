import json
import time

def solution() -> int:
    multi = [1,2,3,4,5,6,7,8,9]
    max_con_product = 0
    for i in range(9999):
        concat = ''.join([str(i*m) for m in multi[:9//len(str(i))]])
        uniq_digits = set(concat)
        if len(concat) == len(uniq_digits) and '0' not in uniq_digits:
            max_con_product = max(max_con_product, int(concat))
    return max_con_product


cpu_s, wall_s = time.process_time(), time.time()
result = solution()
cpu_e, wall_e = time.process_time(), time.time()

cpu_time, wall_time = cpu_e - cpu_s, wall_e - wall_s
print(json.dumps({"solution": result, "cpu": cpu_time, "wall": wall_time}))
