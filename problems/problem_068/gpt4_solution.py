import json
import time

# START - CODE GENERATED BY gpt4
def solution():
    from itertools import permutations

    def is_valid_5gon(perm):
        # Check if the 5-gon ring is valid
        total = perm[0] + perm[5] + perm[6]
        for i in range(1, 5):
            if perm[i] + perm[i + 5] + perm[(i + 1) % 5 + 5] != total:
                return False
        return True

    def get_5gon_string(perm):
        # Create the string representation of the 5-gon ring
        min_external_index = min(range(5), key=lambda i: perm[i])
        result = []
        for i in range(5):
            index = (min_external_index + i) % 5
            result.append(f"{perm[index]}{perm[index + 5]}{perm[(index + 1) % 5 + 5]}")
        return ''.join(result)

    max_string = ""
    for perm in permutations(range(1, 11)):
        if is_valid_5gon(perm):
            current_string = get_5gon_string(perm)
            if len(current_string) == 16:
                max_string = max(max_string, current_string)

    return int(max_string)
# END - CODE GENERATED BY gpt4

cpu_s, wall_s = time.process_time(), time.time()
result = solution()
cpu_e, wall_e = time.process_time(), time.time()

cpu_time, wall_time = cpu_e - cpu_s, wall_e - wall_s
print(json.dumps({"solution": result, "cpu": cpu_time, "wall": wall_time}))
