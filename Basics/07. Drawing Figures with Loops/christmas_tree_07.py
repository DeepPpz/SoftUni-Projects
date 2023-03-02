n = int(input())

for i in range(0, n + 1):
    print(' ' * (n - i), end= '')
    print('*' * i, end= ' ')
    print('|', end= ' ')
    print('*' * i)