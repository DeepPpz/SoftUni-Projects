rows = int(input())
matrix = [[int(x) for x in input().split()] for _ in range(rows)]
sum_diagonal = 0

for i in range(rows):
    sum_diagonal += matrix[i][i]

print(sum_diagonal)
