def is_path(r, c):
    if r < 0 or r >= rows:
        return False
    elif c < 0 or c >= cols:
        return False
    elif labyrinth[r][c] == "*":
        return False
    elif labyrinth[r][c] == "v":
        return False
    else:
        return True


def find_paths(r, c, direction, lab, path):
    if not is_path(r, c):
        return

    if labyrinth[r][c] == "e":
        path.append(direction)
        print(*path, sep='')
    else:
        labyrinth[r][c] = "v"
        path.append(direction)
        find_paths(r - 1, c, "U", lab, path)
        find_paths(r + 1, c, "D", lab, path)
        find_paths(r, c - 1, "L", lab, path)
        find_paths(r, c + 1, "R", lab, path)
        lab[r][c] = "-"
    path.pop()


rows = int(input())
cols = int(input())
labyrinth = []

for _ in range(rows):
    labyrinth.append(list(input()))

find_paths(0, 0, "", labyrinth, [])
