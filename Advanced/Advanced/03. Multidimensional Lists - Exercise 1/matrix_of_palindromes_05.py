rows, cols = map(int, input().split())
START = 97
matrix = []

for r in range(rows):
    matrix.append([])
    for c in range(cols):
        curr_palindrome = chr(START + r) + chr(START + r + c) + chr(START + r)
        matrix[r].append(curr_palindrome)

for r in range(rows):
    print(*matrix[r], sep=' ')
