rows = int(input())
matrix = [[int(x) for x in input().split()] for _ in range(rows)]

primary_diagonal = [matrix[r][r] for r in range(rows)]
secondary_diagonal = [matrix[r][rows - 1 - r] for r in range(rows)]

diff = abs(sum(primary_diagonal) - sum(secondary_diagonal))
print(diff)
