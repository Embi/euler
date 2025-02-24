import json
import time

# START - CODE GENERATED BY gpt4
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

def generate_patterns(length):
    from itertools import combinations
    patterns = []
    for r in range(1, length):
        for indices in combinations(range(length), r):
            pattern = ['*'] * length
            for index in indices:
                pattern[index] = '{}'
            patterns.append(''.join(pattern))
    return patterns

def generate_numbers(pattern, digit):
    return [int(pattern.format(*[digit] * pattern.count('{}'))) for digit in range(10)]

def solution():
    from itertools import count
    for length in count(2):
        patterns = generate_patterns(length)
        for pattern in patterns:
            for digit in range(10):
                if pattern[0] == '{}' and digit == 0:
                    continue
                numbers = generate_numbers(pattern, digit)
                prime_family = [n for n in numbers if is_prime(n)]
                if len(prime_family) >= 8:
                    return min(prime_family)
# END - CODE GENERATED BY gpt4

cpu_s, wall_s = time.process_time(), time.time()
result = solution()
cpu_e, wall_e = time.process_time(), time.time()

cpu_time, wall_time = cpu_e - cpu_s, wall_e - wall_s
print(json.dumps({"solution": result, "cpu": cpu_time, "wall": wall_time}))
