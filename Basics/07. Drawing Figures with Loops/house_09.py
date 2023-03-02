import math

n = int(input())

height = math.ceil(n / 2)
stars = 0

#roof
for roof in range(1, height + 1):
    print('-' * (height - roof), end= '')

    if roof == 1:
        if n % 2 == 0: stars = 2
        else: stars = 1
    else:
        stars += 2
    print('*' * stars, end= '')

    print('-' * (height - roof))

#base
for base in range(1, n // 2 + 1):
    print('|', end= '')
    print('*' * (n - 2), end= '')
    print('|')