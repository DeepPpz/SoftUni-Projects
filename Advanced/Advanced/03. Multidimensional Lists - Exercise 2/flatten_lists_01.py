matrix = [[int(x) for x in row.split()] for row in input().split('|')]
flattened_matrix = [num for sublist in reversed(matrix) for num in sublist]

print(*flattened_matrix, sep=' ')
