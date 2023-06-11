def in_range(i, j):
    return 0 <= i < rows and 0 <= j < cols


def find_player():
    for curr_row in range(rows):
        if "B" in field[curr_row]:
            return curr_row, field[curr_row].index("B")


rows, cols = map(int, input().split())
field = [[x for x in input().split()] for _ in range(rows)]
directions = {
    "up": (-1, 0),
    "down": (1, 0),
    "right": (0, 1),
    "left": (0, -1)
}

row, col = find_player()
total_moves = 0
touched_opponents = 0
while True:
    move = input()
    if move == 'Finish':
        break

    r, c = directions[move]
    if not in_range(row + r, col + c) or field[row + r][col + c] == 'O':
        continue
    else:
        total_moves += 1

    row, col = row + r, col + c
    if field[row][col] == 'P':
        touched_opponents += 1
        field[row][col] = '-'
        if touched_opponents == 3:
            break

print('Game over!')
print(f'Touched opponents: {touched_opponents} Moves made: {total_moves}')
