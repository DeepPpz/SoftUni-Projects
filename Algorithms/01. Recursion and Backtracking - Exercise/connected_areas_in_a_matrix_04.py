def is_path(row, col):
    if row < 0 or row >= rows:
        return False
    elif col < 0 or col >= cols:
        return False
    elif matrix[row][col] == "*":
        return False
    elif matrix[row][col] == "v":
        return False
    return True


def find_areas(r, c, rows, cols, dots, board):
    if not is_path(r, c):
        return

    area_size.append(1)
    matrix[r][c] = "v"

    find_areas(r + 1, c, rows, cols, area_size, matrix)
    find_areas(r - 1, c, rows, cols, area_size, matrix)
    find_areas(r, c + 1, rows, cols, area_size, matrix)
    find_areas(r, c - 1, rows, cols, area_size, matrix)


rows = int(input())
cols = int(input())
matrix = []
areas = {}

for row in range(rows):
    matrix.append(list(input()))

for row in range(rows):
    for col in range(cols):
        if matrix[row][col] == "-":
            area_size = []
            find_areas(row, col, rows, cols, area_size, matrix)
            areas[tuple((row, col))] = sum(area_size)

print(f"Total areas found: {len(areas)}")
i = 0
sorted_areas = dict(sorted(areas.items(), key=lambda x: -x[1]))
for key, value in sorted_areas.items():
    i += 1
    print(f"Area #{i} at {key}, size: {value}")
