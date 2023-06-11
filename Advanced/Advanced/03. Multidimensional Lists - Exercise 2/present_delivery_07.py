def in_range(i, j):
    return 0 <= i < SIZE and 0 <= j < SIZE


presents = int(input())
SIZE = int(input())
neighborhood = list([[x for x in input().split()] for _ in range(SIZE)])
kids_presents = 0
directions = {
    'up': (-1, 0),
    'down': (1, 0),
    'left': (0, -1),
    'right': (0, 1)
}

santa = tuple()
nice_kids = 0
for row in range(SIZE):
    if 'S' in neighborhood[row]:
        santa = (row, neighborhood[row].index('S'))
        neighborhood[row][santa[1]] = '-'
    if 'V' in neighborhood[row]:
        nice_kids += neighborhood[row].count('V')

row, col = santa
curr_move = input()
while curr_move != 'Christmas morning':
    r, c = directions[curr_move]
    row, col = row + r, col + c

    if not in_range(row, col):
        continue
    if neighborhood[row][col] == 'V':
        presents -= 1
        kids_presents += 1
    elif neighborhood[row][col] == 'C':
        for move in directions.values():
            temp_row, temp_col = row + move[0], col + move[1]
            if neighborhood[temp_row][temp_col] == 'X':
                presents -= 1
            elif neighborhood[temp_row][temp_col] == 'V':
                presents -= 1
                kids_presents += 1
            neighborhood[temp_row][temp_col] = '-'

            if not presents:
                break

    neighborhood[row][col] = '-'

    if not presents or nice_kids - kids_presents <= 0:
        break
    curr_move = input()

neighborhood[row][col] = 'S'
if not presents and nice_kids - kids_presents > 0:
    print('Santa ran out of presents!')
[print(*row, sep=' ') for row in neighborhood]
if nice_kids - kids_presents > 0:
    print(f'No presents for {nice_kids - kids_presents} nice kid/s.')
else:
    print(f'Good job, Santa! {kids_presents} happy nice kid/s.')
