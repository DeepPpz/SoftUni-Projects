def is_path(r, c):
    if r >= rows:
        return False
    elif c >= cols:
        return False
    return True


def find_unique_paths(r, c, rows, cols):
    if r == (rows - 1) and c == (cols - 1):
        return 1
    elif is_path(r, c):
        paths = 0
        paths += find_unique_paths(r + 1, c, rows, cols)
        paths += find_unique_paths(r, c + 1, rows, cols)
        return paths
    else:
        return 0


rows = int(input())
cols = int(input())

print(find_unique_paths(0, 0, rows, cols))
