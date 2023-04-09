def is_path(row, col):
    if row < 0 or row >= rows:
        return False
    elif col < 0 or col >= cols:
        return False
    elif labyrinth[row][col] == "#":
        return False
    elif labyrinth[row][col] == "v":
        return False
    return True


def is_exit(row, col):
    if row < 0 or row >= rows:
        return True
    elif col < 0 or col >= cols:
        return True
    return False


def find_paths(r, c, rows, cols, moves, path, lab):
    if is_exit(r, c):
        moves.append(path)
        return
    elif not is_path(r, c):
        return
    else:
        lab[r][c] = "v"
        path += 1
        find_paths(r - 1, c, rows, cols, moves, path, lab)
        find_paths(r + 1, c, rows, cols, moves, path, lab)
        find_paths(r, c - 1, rows, cols, moves, path, lab)
        find_paths(r, c + 1, rows, cols, moves, path, lab)
        lab[r][c] = ""
    path -= 1


rows = int(input())

labyrinth = []
for _ in range(rows):
    labyrinth.append(list(input()))

cols = len(labyrinth[0])
path = 0
moves = []

for r in range(len(labyrinth)):
    if "k" in labyrinth[r]:
        c = labyrinth[r].index("k")
        find_paths(r, c, rows, cols, moves, path, labyrinth)
        break

if moves:
    print(f"Kate got out in {max(moves)} moves")
else:
    print("Kate cannot get out")
