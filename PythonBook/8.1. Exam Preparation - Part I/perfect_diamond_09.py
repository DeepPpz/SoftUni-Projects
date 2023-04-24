n = int(input())
length = 1

for i in range(1, n + 1):
    print(" " * (n - i), end='')
    for j in range(1, length + 1):
        if j % 2 == 0:
            print("-", end='')
        else:
            print("*", end='')
    print(" " * (n - i))
    length += 2

length -= 2

for i in range(n - 1, 0, - 1):
    length -= 2
    print(" " * (n - i), end='')
    for j in range(1, length + 1):
        if j % 2 == 0:
            print("-", end='')
        else:
            print("*", end='')
    print(" " * (n - i))
