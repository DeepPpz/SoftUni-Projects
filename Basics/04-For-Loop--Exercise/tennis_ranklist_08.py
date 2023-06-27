import math

tournament_count = int(input())
entry_points = int(input())

total_points = entry_points
average_points = 0
win_rate = 0

for rank_list in range(tournament_count):
    stage = input()  # W, F or SF
    if stage == 'W':
        total_points += 2000
        win_rate += 1
    elif stage == 'F':
        total_points += 1200
    elif stage == 'SF':
        total_points += 720

average_points = (total_points - entry_points) / tournament_count
win_rate = win_rate / tournament_count * 100

print(f'Final points: {total_points}')
print(f'Average points: {math.floor(average_points)}')
print(f'{win_rate:.2f}%')
