from collections import deque

programmer_time = deque([int(x) for x in input().split()])
all_tasks = deque([int(x) for x in input().split()])
ducks = {'Darth Vader Ducky': 0, 'Thor Ducky': 0,
         'Big Blue Rubber Ducky': 0, 'Small Yellow Rubber Ducky': 0}

while all_tasks:
    time = programmer_time.popleft()
    tasks = all_tasks.pop()
    total_time = time * tasks

    if total_time <= 60:
        ducks['Darth Vader Ducky'] += 1
    elif total_time <= 120:
        ducks['Thor Ducky'] += 1
    elif total_time <= 180:
        ducks['Big Blue Rubber Ducky'] += 1
    elif total_time <= 240:
        ducks['Small Yellow Rubber Ducky'] += 1
    else:
        tasks -= 2
        programmer_time.append(time)
        all_tasks.append(tasks)

print('Congratulations, all tasks have been completed! Rubber ducks rewarded:')
for (duck, count) in ducks.items():
    print(f'{duck}: {count}')
