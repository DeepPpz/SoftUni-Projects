goal = 10000
total_steps = 0

steps = input()

while True:
    if steps == 'Going home':
        steps = int(input())
        total_steps += steps
        break

    steps = int(steps)
    total_steps += steps

    if total_steps >= goal:
        break

    steps = input()

if total_steps >= goal:
    print('Goal reached! Good job!')
    print(f'{total_steps - goal} steps over the goal!')
else:
    print(f'{goal - total_steps} more steps to reach goal.')
