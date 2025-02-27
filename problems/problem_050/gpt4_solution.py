import json
import time

# START - CODE GENERATED BY gpt4
def solution():
    def is_prime(n):
        if n < 2:
            return False
        if n in (2, 3):
            return True
        if n % 2 == 0 or n % 3 == 0:
            return False
        i = 5
        while i * i <= n:
            if n % i == 0 or n % (i + 2) == 0:
                return False
            i += 6
        return True

    def generate_primes(limit):
        primes = []
        for num in range(2, limit):
            if is_prime(num):
                primes.append(num)
        return primes

    limit = 1000000
    primes = generate_primes(limit)
    prime_set = set(primes)

    max_length = 0
    max_prime = 0

    for start in range(len(primes)):
        for end in range(start + max_length, len(primes)):
            prime_sum = sum(primes[start:end])
            if prime_sum >= limit:
                break
            if prime_sum in prime_set:
                current_length = end - start
                if current_length > max_length:
                    max_length = current_length
                    max_prime = prime_sum

    return max_prime
# END - CODE GENERATED BY gpt4

cpu_s, wall_s = time.process_time(), time.time()
result = solution()
cpu_e, wall_e = time.process_time(), time.time()

cpu_time, wall_time = cpu_e - cpu_s, wall_e - wall_s
print(json.dumps({"solution": result, "cpu": cpu_time, "wall": wall_time}))
