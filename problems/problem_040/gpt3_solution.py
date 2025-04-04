import json
import time

# START - CODE GENERATED BY gpt3
def solution():
    # create a string of concatenated positive integers
    num_str = ""
    for i in range(1, 1000000):
        num_str += str(i)

    # find the product of the specified digits
    product = 1
    for i in range(7):
        digit = int(num_str[10**i - 1])
        product *= digit

    return product
# END - CODE GENERATED BY gpt3

cpu_s, wall_s = time.process_time(), time.time()
result = solution()
cpu_e, wall_e = time.process_time(), time.time()

cpu_time, wall_time = cpu_e - cpu_s, wall_e - wall_s
print(json.dumps({"solution": result, "cpu": cpu_time, "wall": wall_time}))