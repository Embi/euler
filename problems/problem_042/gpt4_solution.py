import json
import time

# START - CODE GENERATED BY gpt4
def solution():
    # Read the words from the file
    with open('p042_words.txt', 'r') as file:
        words = file.read().replace('"', '').split(',')

    # Function to calculate the word value
    def word_value(word):
        return sum(ord(char) - ord('A') + 1 for char in word)

    # Generate triangle numbers up to a reasonable limit
    triangle_numbers = set()
    n = 1
    while True:
        triangle_number = n * (n + 1) // 2
        if triangle_number > 26 * 20:  # 26 * 20 is a rough upper limit for word values
            break
        triangle_numbers.add(triangle_number)
        n += 1

    # Count how many words are triangle words
    triangle_word_count = sum(1 for word in words if word_value(word) in triangle_numbers)

    return triangle_word_count
# END - CODE GENERATED BY gpt4

cpu_s, wall_s = time.process_time(), time.time()
result = solution()
cpu_e, wall_e = time.process_time(), time.time()

cpu_time, wall_time = cpu_e - cpu_s, wall_e - wall_s
print(json.dumps({"solution": result, "cpu": cpu_time, "wall": wall_time}))
