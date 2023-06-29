from collections import deque

rows, cols = map(int, input().split())
snake_string = input()
matrix = []
idx = 0

for r in range(1, rows + 1):
    curr_row = deque()
    for c in range(cols):
        if idx == len(snake_string):
            idx = 0

        if r % 2 == 0:
            curr_row.appendleft(snake_string[idx])
        else:
            curr_row.append(snake_string[idx])
        idx += 1
    matrix.append(list(curr_row))

[print(*matrix[r], sep='') for r in range(rows)]
