rows, cols = map(int, input().split(", "))
matrix = [[int(x) for x in input().split(", ")] for _ in range(rows)]
max_submatrix = []
max_sum = 0

for r in range(rows - 1):
    for c in range(cols - 1):
        curr_sum = matrix[r][c] + matrix[r][c+1] + matrix[r+1][c] + matrix[r+1][c+1]
        if curr_sum > max_sum:
            max_submatrix = [[matrix[r][c], matrix[r][c+1]], [matrix[r+1][c], matrix[r+1][c+1]]]
            max_sum = curr_sum

for i in range(len(max_submatrix)):
    print(*max_submatrix[i], sep=' ')
print(max_sum)
