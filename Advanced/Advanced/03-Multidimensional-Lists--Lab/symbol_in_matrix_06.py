size = int(input())
matrix = [[x for x in input()] for _ in range(size)]
target_symbol = input()
is_found = False

for r in range(size):
    if target_symbol in matrix[r]:
        c = matrix[r].index(target_symbol)
        coordinates = (r, c)
        is_found = True
        break

if is_found:
    print(coordinates)
else:
    print(f"{target_symbol} does not occur in the matrix")
