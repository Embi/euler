import json
import time

# START - CODE GENERATED BY gpt4
def solution():
    # Read the file and parse the names
    with open('p022_names.txt', 'r') as file:
        names = file.read().replace('"', '').split(',')

    # Sort the names alphabetically
    names.sort()

    # Function to calculate the alphabetical value of a name
    def name_value(name):
        return sum(ord(char) - ord('A') + 1 for char in name)

    # Calculate the total score
    total_score = 0
    for index, name in enumerate(names):
        # Calculate the score for each name
        score = (index + 1) * name_value(name)
        total_score += score

    return total_score
# END - CODE GENERATED BY gpt4

cpu_s, wall_s = time.process_time(), time.time()
result = solution()
cpu_e, wall_e = time.process_time(), time.time()

cpu_time, wall_time = cpu_e - cpu_s, wall_e - wall_s
print(json.dumps({"solution": result, "cpu": cpu_time, "wall": wall_time}))
