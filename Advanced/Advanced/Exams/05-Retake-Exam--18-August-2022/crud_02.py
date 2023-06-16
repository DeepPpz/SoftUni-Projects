size = 6
matrix = [[x for x in input().split()] for _ in range(size)]
row, col = map(int, input().lstrip('(').rstrip(')').split(', '))
directions = {
    "up": (-1, 0),
    "down": (1, 0),
    "left": (0, -1),
    "right": (0, 1)
}

while True:
    command = input().split(', ')

    if command[0] == 'Stop':
        break

    r, c = directions[command[1]]
    row, col = row + r, col + c

    if command[0] == 'Create' and matrix[row][col] == '.':
        matrix[row][col] = command[2]

    elif command[0] == 'Update' and matrix[row][col] != '.':
        matrix[row][col] = command[2]

    elif command[0] == 'Delete' and matrix[row][col] != '.':
        matrix[row][col] = '.'

    elif command[0] == 'Read' and matrix[row][col] != '.':
        print(matrix[row][col])

[print(*matrix[row]) for row in range(size)]
