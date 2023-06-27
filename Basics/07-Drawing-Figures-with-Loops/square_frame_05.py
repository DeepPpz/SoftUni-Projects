n = int(input())

for row in range(1, n + 1):
    for col in range(1, n + 1):
        if col == 1 or col == n:
            if row == 1 or row == n:
                print('+', end=' ')
            else:
                print('|', end=' ')
        else:
            print('-', end=' ')
    print()
