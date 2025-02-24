import json
import time

first_days = [1, 32, 60, 91, 121, 152, 182, 213, 244, 274, 305, 335]
first_days_leap = [1, 32, 61, 92, 123, 153, 183, 214, 245, 275, 306, 336]

def _is_leap(year):
    if (year % 4) != 0:
        return False
    if (year % 100) == 0 & (year % 400) != 0:
        return False
    return True

def generate_sundays():
    day = 0
    year = 1900
    is_leap = False
    while year < 2000:
        if is_leap:
           yield int(day in first_days_leap)
        else:
           yield int(day in first_days)
        day += 7
        if day >= 365:
            if is_leap:
                year += day // 366
                day = day % 366
            else:
                year += day // 365
                day = day % 365
            is_leap = _is_leap(year)

def solution() -> int:
    return sum(list(generate_sundays()))


cpu_s, wall_s = time.process_time(), time.time()
result = solution()
cpu_e, wall_e = time.process_time(), time.time()

cpu_time, wall_time = cpu_e - cpu_s, wall_e - wall_s
print(json.dumps({"solution": result, "cpu": cpu_time, "wall": wall_time}))
