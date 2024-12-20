import json
import time

# START - CODE GENERATED BY gpt4
def solution():
    def collatz_length(n, cache):
        original_n = n
        length = 0
        while n != 1:
            if n < original_n and n in cache:
                length += cache[n]
                break
            if n % 2 == 0:
                n //= 2
            else:
                n = 3 * n + 1
            length += 1
        cache[original_n] = length
        return length

    max_length = 0
    max_starting_number = 0
    cache = {}

    for i in range(1, 1000000):
        length = collatz_length(i, cache)
        if length > max_length:
            max_length = length
            max_starting_number = i

    return max_starting_number
# END - CODE GENERATED BY gpt4

cpu_s, wall_s = time.process_time(), time.time()
result = solution()
cpu_e, wall_e = time.process_time(), time.time()

cpu_time, wall_time = cpu_e - cpu_s, wall_e - wall_s
print(json.dumps({"solution": result, "cpu": cpu_time, "wall": wall_time}))
