import json
import time

# START - CODE GENERATED BY gpt4
def solution():
    def minimal_x(D):
        m, d, a = 0, 1, int(D**0.5)
        num1, num = 1, a
        den1, den = 0, 1
        while num*num - D*den*den != 1:
            m = d*a - m
            d = (D - m*m) // d
            a = (int(D**0.5) + m) // d
            num2, num1 = num1, num
            den2, den1 = den1, den
            num = a*num1 + num2
            den = a*den1 + den2
        return num

    max_x = 0
    result_D = 0
    for D in range(2, 1001):
        if int(D**0.5)**2 == D:
            continue
        x = minimal_x(D)
        if x > max_x:
            max_x = x
            result_D = D

    return result_D
# END - CODE GENERATED BY gpt4

cpu_s, wall_s = time.process_time(), time.time()
result = solution()
cpu_e, wall_e = time.process_time(), time.time()

cpu_time, wall_time = cpu_e - cpu_s, wall_e - wall_s
print(json.dumps({"solution": result, "cpu": cpu_time, "wall": wall_time}))
