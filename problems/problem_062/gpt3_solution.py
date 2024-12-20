import json
import time

# START - CODE GENERATED BY gpt3
def solution():
    cubes = {}
    i = 1
    while True:
        cube = i ** 3
        digits = ''.join(sorted(str(cube)))
        if digits in cubes:
            cubes[digits].append(cube)
            if len(cubes[digits]) == 5:
                return cubes[digits][0]
        else:
            cubes[digits] = [cube]
        i += 1
# END - CODE GENERATED BY gpt3

cpu_s, wall_s = time.process_time(), time.time()
result = solution()
cpu_e, wall_e = time.process_time(), time.time()

cpu_time, wall_time = cpu_e - cpu_s, wall_e - wall_s
print(json.dumps({"solution": result, "cpu": cpu_time, "wall": wall_time}))