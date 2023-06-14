def find_submarine(field):
    for curr_row in range(size):
        if "S" in field[curr_row]:
            return curr_row, field[curr_row].index("S")


size = int(input())
battlefield = [[x for x in input()] for _ in range(size)]
mines_hit = 0
cruisers_hit = 0
directions = {
    "up": (-1, 0),
    "down": (1, 0),
    "left": (0, -1),
    "right": (0, 1)
}

row, col = find_submarine(battlefield)
battlefield[row][col] = '-'
while True:
    r, c = directions[input()]
    row, col = row + r, col + c

    if battlefield[row][col] == '*':
        battlefield[row][col] = '-'
        mines_hit += 1

        if mines_hit == 3:
            battlefield[row][col] = 'S'
            print(f'Mission failed, U-9 disappeared! Last known coordinates [{row}, {col}]!')
            break

    if battlefield[row][col] == 'C':
        battlefield[row][col] = '-'
        cruisers_hit += 1

        if cruisers_hit == 3:
            battlefield[row][col] = 'S'
            print('Mission accomplished, U-9 has destroyed all battle cruisers of the enemy!')
            break

[print(''.join(row)) for row in battlefield]
