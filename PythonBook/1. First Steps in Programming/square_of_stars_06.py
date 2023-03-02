n = int(input())

for i in range(1, n + 1):
    if i == 1:
        print('*' * n)
    elif i == n:
        print('*' * n)
    else:
        m = n - 2
        print('*', end='')
        print(" " * m, end='')
        print("*")