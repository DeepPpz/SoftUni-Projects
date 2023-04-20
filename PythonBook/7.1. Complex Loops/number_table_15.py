n = int(input())

for row in range(n):
    for col in range(n):
        num = row + col + 1

        if num > n:
            num = 2 * n - num

        print(num, end=' ')

    print()
