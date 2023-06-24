def in_range(i, j):
    return 0 <= i < rows and 0 <= j < cols


rows, cols = map(int, input().split(','))
cupboard = [[x for x in input()] for _ in range(rows)]
directions = {
    "left": (0, -1),
    "right": (0, 1),
    "up": (-1, 0),
    "down": (1, 0)
}

total_cheese = 0
mouse = tuple()
for row in range(rows):
    if 'M' in cupboard[row]:
        mouse = (row, cupboard[row].index('M'))
        cupboard[row][mouse[1]] = '*'
    if 'C' in cupboard[row]:
        total_cheese += cupboard[row].count('C')

row, col = mouse
while True:
    command = input()

    if command == 'danger':
        cupboard[row][col] = 'M'
        print('Mouse will come back later!')
        break
    else:
        r, c = directions[command]
        new_row, new_col = row + r, col + c

    if not in_range(new_row, new_col):
        cupboard[row][col] = 'M'
        print('No more cheese for tonight!')
        break

    elif cupboard[new_row][new_col] == 'C':
        total_cheese -= 1
        cupboard[new_row][new_col] = '*'

        if total_cheese == 0:
            cupboard[new_row][new_col] = 'M'
            print('Happy mouse! All the cheese is eaten, good night!')
            break

    elif cupboard[new_row][new_col] == 'T':
        cupboard[new_row][new_col] = 'M'
        print('Mouse is trapped!')
        break

    elif cupboard[new_row][new_col] == '@':
        continue

    row, col = new_row, new_col

[print(*cupboard[row], sep='') for row in range(rows)]
