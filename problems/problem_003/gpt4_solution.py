import json
import time

# START - CODE GENERATED BY gpt4
def solution():
    def largest_prime_factor(n):
        # Start with the smallest prime factor
        factor = 2
        # Divide n by factor until it is no longer divisible
        while n % factor == 0:
            n //= factor
        # Check for odd factors from 3 onwards
        factor = 3
        while factor * factor <= n:
            while n % factor == 0:
                n //= factor
            factor += 2
        # If n becomes a prime number greater than 2
        if n > 2:
            return n
        return factor

    return largest_prime_factor(600851475143)
# END - CODE GENERATED BY gpt4

cpu_s, wall_s = time.process_time(), time.time()
result = solution()
cpu_e, wall_e = time.process_time(), time.time()

cpu_time, wall_time = cpu_e - cpu_s, wall_e - wall_s
print(json.dumps({"solution": result, "cpu": cpu_time, "wall": wall_time}))