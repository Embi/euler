#!/usr/bin/env python

import json
import time

dictionary = {
    1: "one",
    2: "two",
    3: "three",
    4: "four",
    5: "five",
    6: "six",
    7: "seven",
    8: "eight",
    9: "nine",
    10: "ten",
    11: "eleven",
    12: "twelve",
    13: "thirteen",
    14: "fourteen",
    15: "fifteen",
    16: "sixteen",
    17: "seventeen",
    18: "eighteen",
    19: "nineteen",
    20: "twenty",
    30: "thirty",
    40: "forty",
    50: "fifty",
    60: "sixty",
    70: "seventy",
    80: "eighty",
    90: "ninety",
}

def solution() -> int:
    letter_count = 0
    for i in range(1, 1001):
        words = ""
        thousands = i // 1000
        hundreds = (i % 1000) // 100
        less_then_hundred = (i % 100)
        if thousands > 0:
            words += f'{dictionary[thousands]}thousand'
        if hundreds > 0:
            words += f'{dictionary[hundreds]}hundred'
        if less_then_hundred > 0:
            if len(words) > 0:
                words += 'and'
        if less_then_hundred > 19:
            ones = less_then_hundred % 10
            tens = (less_then_hundred // 10) * 10
            words += f'{dictionary[tens]}'
            if ones > 0:
                words += f'{dictionary[ones]}'
        elif less_then_hundred > 0:
            words += f'{dictionary[less_then_hundred]}'
        letter_count += len(words)
    return letter_count

cpu_s, wall_s = time.process_time(), time.time()
result = solution()
cpu_e, wall_e = time.process_time(), time.time()

cpu_time, wall_time = cpu_e - cpu_s, wall_e - wall_s
print(json.dumps({"solution": result, "cpu": cpu_time, "wall": wall_time}))
