def in_range(i, j):
    return 0 <= i < rows and 0 <= j < cols


def find_player(size, lab):
    for curr_row in range(size):
        if "P" in lab[curr_row]:
            return curr_row, lab[curr_row].index("P")


def find_bunnies(rows, cols, lab):
    temp_list = []
    for row in range(rows):
        for col in range(cols):
            if lab[row][col] == "B":
                temp_list.append((row, col))
    return temp_list


def bunny_spread(total_bunnies, lab):
    for b_row, b_col in total_bunnies:
        for s_row, s_col in directions.values():
            new_row = b_row + s_row
            new_col = b_col + s_col

            if in_range(new_row, new_col):
                lab[new_row][new_col] = 'B'


rows, cols = map(int, input().split())
labyrinth = [[x for x in input()] for _ in range(rows)]
moves = [x for x in input()]
end_result = ''
directions = {
    "L": (0, -1),
    "U": (-1, 0),
    "R": (0, 1),
    "D": (1, 0)
}

p_row, p_col = find_player(rows, labyrinth)
labyrinth[p_row][p_col] = '.'

for move in moves:
    r, c = directions[move]
    p_row, p_col = p_row + r, p_col + c

    bunnies = find_bunnies(rows, cols, labyrinth)
    bunny_spread(bunnies, labyrinth)

    if not in_range(p_row, p_col):
        p_row, p_col = p_row - r, p_col - c
        end_result = f'won: {p_row} {p_col}'
        break

    elif labyrinth[p_row][p_col] == 'B':
        end_result = f'dead: {p_row} {p_col}'
        break

[print(''.join(labyrinth[row])) for row in range(rows)]
print(end_result)
