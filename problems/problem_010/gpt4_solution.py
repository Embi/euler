import json
import time

# START - CODE GENERATED BY gpt4
def solution():
    def is_prime(n):
        if n <= 1:
            return False
        if n <= 3:
            return True
        if n % 2 == 0 or n % 3 == 0:
            return False
        i = 5
        while i * i <= n:
            if n % i == 0 or n % (i + 2) == 0:
                return False
            i += 6
        return True

    def sum_of_primes_below(limit):
        if limit < 2:
            return 0
        sum_primes = 2
        for num in range(3, limit, 2):
            if is_prime(num):
                sum_primes += num
        return sum_primes

    return sum_of_primes_below(2000000)
# END - CODE GENERATED BY gpt4

cpu_s, wall_s = time.process_time(), time.time()
result = solution()
cpu_e, wall_e = time.process_time(), time.time()

cpu_time, wall_time = cpu_e - cpu_s, wall_e - wall_s
print(json.dumps({"solution": result, "cpu": cpu_time, "wall": wall_time}))