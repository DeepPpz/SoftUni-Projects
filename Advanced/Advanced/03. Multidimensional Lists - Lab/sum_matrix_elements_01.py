rows, cols = map(int, input().split(", "))
matrix = [[int(x) for x in input().split(", ")] for _ in range(rows)]
total_sum = sum([sum(x) for x in matrix])

print(total_sum)
print(matrix)
