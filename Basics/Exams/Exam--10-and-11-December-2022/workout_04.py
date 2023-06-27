import math

n_days = int(input())
first_day = float(input())

day_km = 0
total_km = 0
goal_flag = False

for days in range(0, n_days + 1):
    if days == 0:
        day_km += first_day
        total_km += first_day
        continue

    k_add = int(input())
    k_add /= 100

    day_km += day_km * k_add
    total_km += day_km

    if total_km >= 1000:
        goal_flag = True

if goal_flag:
    print(f"You've done a great job running {math.ceil(total_km - 1000)} more kilometers!")
else:
    print(f'Sorry Mrs. Ivanova, you need to run {math.ceil(1000 - total_km)} more kilometers')
