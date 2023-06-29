def validate_index(idx, max_len):
    return 0 <= idx < max_len


size = int(input())
matrix = [[int(x) for x in input().split()] for _ in range(size)]
line = input().split()

while line[0] != 'END':
    action = line[0]
    row, col, value = map(int, line[1:])

    if not validate_index(row, size) or not validate_index(col, size):
        print('Invalid coordinates')

    elif action == 'Add':
        matrix[row][col] += value

    elif action == 'Subtract':
        matrix[row][col] -= value

    line = input().split()

[print(*matrix[r], sep=' ') for r in range(size)]
