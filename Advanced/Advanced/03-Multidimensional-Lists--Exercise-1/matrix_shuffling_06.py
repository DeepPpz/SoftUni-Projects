def validate_indexes(r1, c1, r2, c2):
    return r1 < rows and c1 < cols and r2 < rows and c2 < cols


rows, cols = map(int, input().split())
matrix = [[x for x in input().split()] for _ in range(rows)]

while True:
    command = input().split()

    if command[0] == "END":
        break

    if command[0] != "swap" or len(command[1:]) != 4 or any(int(x) < 0 for x in command[1:]):
        print("Invalid input!")
        continue

    row1, col1, row2, col2 = map(int, command[1:])

    if not validate_indexes(row1, col1, row2, col2):
        print("Invalid input!")
        continue

    matrix[row1][col1], matrix[row2][col2] = matrix[row2][col2], matrix[row1][col1]
    print(*[' '.join(x) for x in matrix], sep='\n')
