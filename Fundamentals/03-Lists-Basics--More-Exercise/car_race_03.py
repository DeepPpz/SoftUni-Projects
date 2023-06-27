total_times = input().split()

total_times = list(map(int, total_times))
checkpoints = len(total_times) // 2
left_time, right_time = 0, 0

for check in range(checkpoints):
    if total_times[check] == 0:
        left_time *= 0.80
    else:
        left_time += total_times[check]

for r in range(len(total_times) - 1, checkpoints, - 1):
    if total_times[r] == 0:
        right_time *= 0.80
    else:
        right_time += total_times[r]

if left_time < right_time:
    print(f'The winner is left with total time: {left_time:.1f}')
else:
    print(f'The winner is right with total time: {right_time:.1f}')
