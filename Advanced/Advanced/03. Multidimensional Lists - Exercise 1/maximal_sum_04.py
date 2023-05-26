rows, cols = map(int, input().split())
matrix = [[int(x) for x in input().split()] for _ in range(rows)]
max_sum = float("-inf")
max_matrix = []

for row in range(rows - 2):
    for col in range(cols - 2):
        curr_sum = 0
        curr_matrix = []
        for r in range(row, row + 3):
            curr_matrix.append([matrix[r][c] for c in range(col, col + 3)])
        curr_sum = sum([sum(curr_matrix[r]) for r in range(3)])

        if curr_sum > max_sum:
            max_sum = curr_sum
            max_matrix = curr_matrix

print(f"Sum = {max_sum}")
for r in range(3):
    print(*max_matrix[r], sep=' ')
