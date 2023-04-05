import math

n = int(input())
middle_row = math.ceil(n / 2)

print("*" * 2 * n, end='')
print(" " * n, end='')
print("*" * 2 * n)

for row in range(2, n):
    slashes = "/" * ((2 * n) - 2)
    print("*", end='')
    print(slashes, end='')
    print("*", end='')

    if row == middle_row:
        print("|" * n, end='')
    else:
        print(" " * n, end='')

    print("*", end='')
    print(slashes, end='')
    print("*", end='')
    print()

print("*" * 2 * n, end='')
print(" " * n, end='')
print("*" * 2 * n)
