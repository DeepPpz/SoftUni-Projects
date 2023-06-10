def in_range(i, j):
    return 0 <= i < SIZE and 0 <= j < SIZE


SIZE = int(input())
wonderland = list([[x for x in input().split()] for _ in range(SIZE)])
collected_tea = 0
tea_party = False
directions = {
    'left': (0, -1),
    'right': (0, 1),
    'up': (-1, 0),
    'down': (1, 0)
}

alice, rabbit_hole = tuple(), tuple()
for row in range(SIZE):
    if 'A' in wonderland[row]:
        alice = (row, wonderland[row].index('A'))
    if 'R' in wonderland[row]:
        rabbit_hole = (row, wonderland[row].index('R'))

row, col = alice
wonderland[row][col] = '*'
while True:
    curr_move = input()
    r, c = directions[curr_move]
    row, col = row + r, col + c

    if not in_range(row, col):
        break
    if wonderland[row][col] == 'R':
        wonderland[row][col] = '*'
        break
    if wonderland[row][col].isnumeric():
        collected_tea += int(wonderland[row][col])
    wonderland[row][col] = '*'

    if collected_tea >= 10:
        tea_party = True
        break

if tea_party:
    print('She did it! She went to the party.')
else:
    print("Alice didn't make it to the tea party.")
[print(*row, sep=' ') for row in wonderland]
