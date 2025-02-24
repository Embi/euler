import json
import time

alphabet = {
    'a': 1,
    'b': 2,
    'c': 3,
    'd': 4,
    'e': 5,
    'f': 6,
    'g': 7,
    'h': 8,
    'i': 9,
    'j': 10,
    'k': 11,
    'l': 12,
    'm': 13,
    'n': 14,
    'o': 15,
    'p': 16,
    'q': 17,
    'r': 18,
    's': 19,
    't': 20,
    'u': 21,
    'v': 22,
    'w': 23,
    'x': 24,
    'y': 25,
    'z': 26,
}

with open('p022_names.txt', 'r') as names_file:
    names = names_file.readline()

names = names.lower().replace('"', '').split(',')
names = sorted(names)


def solution() -> int:
    total = 0
    for idx, name in enumerate(names):
        name_alpha_value = sum(map(lambda x: alphabet[x], name))
        name_score = name_alpha_value * (idx + 1)
        total += name_score
    return total

cpu_s, wall_s = time.process_time(), time.time()
result = solution()
cpu_e, wall_e = time.process_time(), time.time()

cpu_time, wall_time = cpu_e - cpu_s, wall_e - wall_s
print(json.dumps({"solution": result, "cpu": cpu_time, "wall": wall_time}))
