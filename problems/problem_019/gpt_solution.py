import json
import time

# START - CODE GENERATED BY GPT
import datetime

def solution():
    count = 0
    for year in range(1901, 2001):
        for month in range(1, 13):
            if datetime.date(year, month, 1).weekday() == 6:
                count += 1
    return count

# Explanation:
# We can use the `datetime` module in Python to easily determine
# the day of the week for a given date. We loop through all the
# years and months in the twentieth century (1901-2000) and check
# if the first day of the month is a Sunday (weekday() returns
# 6 for Sunday). If it is, we increment our count. Finally, we
# return the count of Sundays that fell on the first of the month.
# END - CODE GENERATED BY GPT

cpu_s, wall_s = time.process_time(), time.time()
result = solution()
cpu_e, wall_e = time.process_time(), time.time()

cpu_time, wall_time = cpu_e - cpu_s, wall_e - wall_s
print(json.dumps({"solution": result, "cpu": cpu_time, "wall": wall_time}))