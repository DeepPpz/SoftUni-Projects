from collections import deque


def is_out_of_range(row, col, rows, cols):
    if row < 0 or row >= rows:
        return True
    elif col < 0 or col >= cols:
        return True
    return False


def print_exit(row, col, coals):
    coordinates = (row, col)
    if total_coals - coals == 0:
        print(f"You collected all coal!", coordinates)
    else:
        print(f"{total_coals - coals} pieces of coal left.", coordinates)


def find_path(r, c, rows, cols, coals_collected, field, move=tuple()):
    if is_out_of_range(r, c, rows, cols):
        r = r - move[0]
        c = c - move[1]
    elif field[r][c] == "e":
        print(f"Game over! ({r}, {c})")
        exit(0)
    elif field[r][c] == "c":
        coals_collected += 1
        field[r][c] = "*"

    if not movements:
        print_exit(r, c, coals_collected)
        return
    else:
        move = directions[movements.popleft()]
        find_path(r + move[0], c + move[1], rows, cols, coals_collected, field, move)


size = int(input())
movements = deque([x for x in input().split()])
field = list([[x for x in input().split()] for _ in range(size)])
total_coals = 0
coals_collected = 0
miner = tuple()

directions = {
    "left": (0, -1),
    "right": (0, 1),
    "up": (-1, 0),
    "down": (1, 0)
}

for row in range(size):
    if "c" in field[row]:
        total_coals += field[row].count("c")
    if "s" in field[row]:
        miner = (row, field[row].index("s"))

find_path(miner[0], miner[1], size, size, coals_collected, field)
