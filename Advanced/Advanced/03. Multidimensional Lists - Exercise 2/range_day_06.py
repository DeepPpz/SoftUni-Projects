def in_range(i, j):
    return 0 <= i < SIZE and 0 <= j < SIZE


def find_targets(row, col):
    if not in_range(row, col):
        return 0
    if shooting_field[row][col] == 'x':
        shooting_field[row][col] = '.'
        targets_hit.append([row, col])
        return 1
    else:
        return find_targets(row + r, col + c)


SIZE = 5
shooting_field = [[x for x in input().split()] for _ in range(SIZE)]
directions = {
    'up': (-1, 0),
    'down': (1, 0),
    'left': (0, -1),
    'right': (0, 1)
}

position = tuple()
targets = 0
targets_hit = []
for row in range(SIZE):
    if 'A' in shooting_field[row]:
        position = (row, shooting_field[row].index('A'))
    if 'x' in shooting_field[row]:
        targets += shooting_field[row].count('x')

row, col = position
for _ in range(int(input())):
    command = input().split()
    r, c = directions[command[1]]

    if command[0] == 'move':
        new_row = row + (r * int(command[2]))
        new_col = col + (c * int(command[2]))
        if in_range(new_row, new_col) and shooting_field[new_row][new_col] == '.':
            shooting_field[row][col] = '.'
            row, col = new_row, new_col

    elif command[0] == 'shoot':
        targets -= find_targets(row + r, col + c)
        if not targets:
            break

if targets:
    print(f'Training not completed! {targets} targets left.')
else:
    print(f'Training completed! All {len(targets_hit)} targets hit.')
print(*targets_hit, sep='\n')
