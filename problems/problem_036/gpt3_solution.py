import json
import time

# START - CODE GENERATED BY gpt3
def solution():
    total = 0
    for i in range(1, 1000000):
        if str(i) == str(i)[::-1]: # check if number is palindrome in base 10
            binary = bin(i)[2:] # convert number to binary
            if binary == binary[::-1]: # check if binary representation is palindrome
                total += i
    return total
# END - CODE GENERATED BY gpt3

cpu_s, wall_s = time.process_time(), time.time()
result = solution()
cpu_e, wall_e = time.process_time(), time.time()

cpu_time, wall_time = cpu_e - cpu_s, wall_e - wall_s
print(json.dumps({"solution": result, "cpu": cpu_time, "wall": wall_time}))