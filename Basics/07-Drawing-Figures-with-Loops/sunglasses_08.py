n = int(input())

print('*' * (2 * n), end='')
print(' ' * n, end='')
print('*' * (2 * n), end='')
print()

for i in range(n - 2):
    print('*', end='')
    print('/' * (2 * n - 2), end='')
    print('*', end='')

    if i == (n - 1) // 2 - 1:
        print('|' * n, end='')
    else:
        print(' ' * n, end='')

    print('*', end='')
    print('/' * (2 * n - 2), end='')
    print('*', end='')
    print()

print('*' * (2 * n), end='')
print(' ' * n, end='')
print('*' * (2 * n), end='')
