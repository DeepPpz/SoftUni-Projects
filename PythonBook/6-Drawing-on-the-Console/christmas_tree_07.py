n = int(input())

for i in range(n + 1):
    spaces = " " * (n - i)
    stars = "*" * i
    print(spaces, end='')
    print(stars, end='')
    print(" | ", end='')
    print(stars, end='')
    print(spaces)
