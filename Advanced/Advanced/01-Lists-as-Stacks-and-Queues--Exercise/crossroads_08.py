from collections import deque

green_duration = int(input())
free_duration = int(input())
crossroad = deque()
passed_cars = 0

while True:
    next_car = input()

    if next_car == 'END':
        print(f'Everyone is safe.\n{passed_cars} total cars passed the crossroads.')
        break
    elif next_car != 'green':
        crossroad.append(next_car)
        continue

    green = green_duration

    while crossroad and green > 0:
        curr_car = crossroad.popleft()
        car = len(curr_car)

        if green + free_duration >= car:
            green -= car
            passed_cars += 1
        else:
            crash = curr_car[green + free_duration]
            print(f'A crash happened!\n{curr_car} was hit at {crash}.')
            exit(0)
