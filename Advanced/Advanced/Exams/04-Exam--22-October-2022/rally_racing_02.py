size = int(input())
number_car = input()
race_route = [[x for x in input().split()] for _ in range(size)]
total_km = 0
directions = {
    "left": (0, -1),
    "right": (0, 1),
    "up": (-1, 0),
    "down": (1, 0)
}

tunnel = []
finish = tuple()
for row in range(size):
    if 'T' in race_route[row]:
        tunnel.append((row, race_route[row].index('T')))
    if 'F' in race_route[row]:
        finish = (row, race_route[row].index('F'))

row, col = 0, 0
while True:
    command = input()

    if command == 'End':
        print(f'Racing car {number_car} DNF.')
        break

    r, c = directions[command]
    row, col = row + r, col + c

    if race_route[row][col] == '.':
        total_km += 10
    elif race_route[row][col] == 'T':
        if (row, col) == tunnel[0]:
            row, col = tunnel[1]
        else:
            row, col = tunnel[0]

        total_km += 30
        race_route[tunnel[0][0]][tunnel[0][1]] = '.'
        race_route[tunnel[1][0]][tunnel[1][1]] = '.'

    elif race_route[row][col] == 'F':
        total_km += 10
        print(f'Racing car {number_car} finished the stage!')
        break

race_route[row][col] = 'C'
print(f'Distance covered {total_km} km.')
[print(*race_route[i], sep='') for i in range(len(race_route))]
