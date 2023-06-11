def in_range(i, j):
    return 0 <= i < size and 0 <= j < size


def find_squirrel():
    for curr_row in range(size):
        if "s" in field[curr_row]:
            return curr_row, field[curr_row].index("s")


size = int(input())
movements = [x for x in input().split(', ')]
field = [[x for x in input()] for _ in range(size)]
hazelnuts = 0
fail = False
directions = {
    "left": (0, -1),
    "right": (0, 1),
    "down": (1, 0),
    "up": (-1, 0)
}

row, col = find_squirrel()
field[row][col] = '*'

for move in movements:
    r, c = directions[move]
    row, col = row + r, col + c

    if not in_range(row, col):
        print('The squirrel is out of the field.')
        fail = True
        break

    if field[row][col] == 't':
        print('Unfortunately, the squirrel stepped on a trap...')
        fail = True
        break

    if field[row][col] == 'h':
        hazelnuts += 1
        field[row][col] = '*'

        if hazelnuts == 3:
            print('Good job! You have collected all hazelnuts!')
            break

if hazelnuts < 3 and not fail:
    print('There are more hazelnuts to collect.')
print(f'Hazelnuts collected: {hazelnuts}')
