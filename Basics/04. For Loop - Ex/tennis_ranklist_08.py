tourn_count = int(input())
entry_points = int(input())

total_points = entry_points
average_points = 0
win_rate = 0

for ranklist in range(tourn_count):
    stage = input() #W, F or SF
    if stage == 'W':
        total_points += 2000
        win_rate += 1
    elif stage == 'F': total_points += 1200
    elif stage == 'SF': total_points += 720

average_points = (total_points - entry_points) / tourn_count
win_rate = win_rate / tourn_count * 100

import math

print(f'Final points: {total_points}')
print(f'Average points: {math.floor(average_points)}')
print(f'{win_rate:.2f}%')