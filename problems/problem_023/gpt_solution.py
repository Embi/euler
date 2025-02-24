import json
import time

# START - CODE GENERATED BY GPT
def solution():
    def proper_divisors(n):
        divisors = [1]
        for i in range(2, int(n**0.5)+1):
            if n % i == 0:
                divisors.append(i)
                if i != n//i:
                    divisors.append(n//i)
        return divisors
    
    abundant_numbers = []
    for i in range(1, 28124):
        if sum(proper_divisors(i)) > i:
            abundant_numbers.append(i)
    
    abundant_sums = set()
    for i in range(len(abundant_numbers)):
        for j in range(i, len(abundant_numbers)):
            if abundant_numbers[i] + abundant_numbers[j] > 28123:
                break
            abundant_sums.add(abundant_numbers[i] + abundant_numbers[j])
    
    non_abundant_sums = set(range(1, 28124)) - abundant_sums
    return sum(non_abundant_sums)
# END - CODE GENERATED BY GPT

cpu_s, wall_s = time.process_time(), time.time()
result = solution()
cpu_e, wall_e = time.process_time(), time.time()

cpu_time, wall_time = cpu_e - cpu_s, wall_e - wall_s
print(json.dumps({"solution": result, "cpu": cpu_time, "wall": wall_time}))