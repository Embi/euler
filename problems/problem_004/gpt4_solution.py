import json
import time

# START - CODE GENERATED BY gpt4
def solution():
    def is_palindrome(n):
        s = str(n)
        return s == s[::-1]

    max_palindrome = 0
    for i in range(100, 1000):
        for j in range(i, 1000):  # Start j from i to avoid duplicate calculations
            product = i * j
            if is_palindrome(product) and product > max_palindrome:
                max_palindrome = product
    return max_palindrome
# END - CODE GENERATED BY gpt4

cpu_s, wall_s = time.process_time(), time.time()
result = solution()
cpu_e, wall_e = time.process_time(), time.time()

cpu_time, wall_time = cpu_e - cpu_s, wall_e - wall_s
print(json.dumps({"solution": result, "cpu": cpu_time, "wall": wall_time}))
