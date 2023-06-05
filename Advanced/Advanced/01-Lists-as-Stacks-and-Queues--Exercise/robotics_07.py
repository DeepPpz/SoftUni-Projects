from collections import deque
from datetime import datetime, timedelta

robots = {}
for r in input().split(';'):
    robot, time = r.split('-')
    robots[robot] = [int(time), 0]

start_time = datetime.strptime(input(), '%H:%M:%S')
products = deque()

while True:
    line = input()

    if line == 'End':
        break
    products.append(line)

end_time = start_time
while products:
    end_time += timedelta(0, 1)
    curr_product = products.popleft()

    free_robots = []
    for robot, time in robots.items():
        if time[1] != 0:
            robots[robot][1] -= 1

        if time[1] == 0:
            free_robots.append([robot, time])

    if not free_robots:
        products.append(curr_product)
        continue

    robot_name, data = free_robots[0]
    robots[robot_name][1] = data[0]

    print(f'{robot_name} - {curr_product} [{end_time.strftime("%H:%M:%S")}]')
