import json
import time

# START - CODE GENERATED BY gpt4
def solution():
    def count_divisors(n):
        count = 0
        sqrt_n = int(n**0.5)
        for i in range(1, sqrt_n + 1):
            if n % i == 0:
                count += 2 if i != n // i else 1
        return count

    n = 1
    triangle_number = 0
    while True:
        triangle_number += n
        if count_divisors(triangle_number) > 500:
            return triangle_number
        n += 1
# END - CODE GENERATED BY gpt4

cpu_s, wall_s = time.process_time(), time.time()
result = solution()
cpu_e, wall_e = time.process_time(), time.time()

cpu_time, wall_time = cpu_e - cpu_s, wall_e - wall_s
print(json.dumps({"solution": result, "cpu": cpu_time, "wall": wall_time}))
