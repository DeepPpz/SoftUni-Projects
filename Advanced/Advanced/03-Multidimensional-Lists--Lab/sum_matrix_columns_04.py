rows, cols = map(int, input().split(", "))
matrix = [[int(x) for x in input().split()] for _ in range(rows)]

for c in range(cols):
    col_sum = 0
    for r in range(rows):
        col_sum += matrix[r][c]
    print(col_sum)
