import json
import time

# START - CODE GENERATED BY gpt4
def solution():
    def is_pandigital(a, b, c):
        digits = str(a) + str(b) + str(c)
        return len(digits) == 9 and set(digits) == set('123456789')

    products = set()

    # Check for 1-digit * 4-digit = 4-digit
    for a in range(1, 10):
        for b in range(1234, 9877):  # 4-digit numbers
            c = a * b
            if c > 9876:  # c must be a 4-digit number
                break
            if is_pandigital(a, b, c):
                products.add(c)

    # Check for 2-digit * 3-digit = 4-digit
    for a in range(12, 98):  # 2-digit numbers
        for b in range(123, 988):  # 3-digit numbers
            c = a * b
            if c > 9876:  # c must be a 4-digit number
                break
            if is_pandigital(a, b, c):
                products.add(c)

    return sum(products)

# END - CODE GENERATED BY gpt4

cpu_s, wall_s = time.process_time(), time.time()
result = solution()
cpu_e, wall_e = time.process_time(), time.time()

cpu_time, wall_time = cpu_e - cpu_s, wall_e - wall_s
print(json.dumps({"solution": result, "cpu": cpu_time, "wall": wall_time}))
