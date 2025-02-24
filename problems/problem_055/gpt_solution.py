import json
import time

# START - CODE GENERATED BY GPT
def is_palindrome(n):
    return str(n) == str(n)[::-1]

def reverse_and_add(n):
    return n + int(str(n)[::-1])

def is_lychrel(n):
    for i in range(50):
        n = reverse_and_add(n)
        if is_palindrome(n):
            return False
    return True

def solution():
    count = 0
    for i in range(1, 10000):
        if is_lychrel(i):
            count += 1
    return count
# END - CODE GENERATED BY GPT

cpu_s, wall_s = time.process_time(), time.time()
result = solution()
cpu_e, wall_e = time.process_time(), time.time()

cpu_time, wall_time = cpu_e - cpu_s, wall_e - wall_s
print(json.dumps({"solution": result, "cpu": cpu_time, "wall": wall_time}))