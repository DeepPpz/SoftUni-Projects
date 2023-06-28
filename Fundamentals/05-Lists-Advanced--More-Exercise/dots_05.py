def is_path(row, col):
    if row < 0 or row >= rows:
        return False
    elif col < 0 or col >= cols:
        return False
    elif board[row][col] != ".":
        return False
    return True


def find_dots(r, c, rows, cols, dots, board):
    if not is_path(r, c):
        return

    dots.append(1)
    max_dots.add(sum(dots))
    board[r][c] = "v"

    find_dots(r + 1, c, rows, cols, dots, board)
    find_dots(r - 1, c, rows, cols, dots, board)
    find_dots(r, c + 1, rows, cols, dots, board)
    find_dots(r, c - 1, rows, cols, dots, board)


rows = int(input())
board = []
max_dots = {0}

for row in range(rows):
    board.append(list(input().split()))
cols = len(board[0])

for row in range(rows):
    for col in range(cols):
        if board[row][col] == ".":
            dots = []
            find_dots(row, col, rows, cols, dots, board)

print(max(max_dots))
