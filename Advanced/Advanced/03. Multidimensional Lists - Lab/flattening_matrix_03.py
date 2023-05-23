rows = int(input())
matrix = [[int(x) for x in input().split(", ")] for _ in range(rows)]

flattened_matrix = [x for sublist in matrix for x in sublist]
print(flattened_matrix)
