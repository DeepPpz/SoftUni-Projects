n = int(input())

left_right = (n - 1) // 2

while left_right >= 0:
    print('-' * left_right, end= '')
    print('*', end= '')

    mid = round(n - 2 * left_right - 2)
    if mid >= 0:
        print('-' * mid, end= '')
        print('*', end= '')

    print('-' * left_right, end= '')
    left_right -= 1
    print()

left_right = 0

for i in range((n - 1) // 2):
    left_right += 1
    print('-' * left_right, end='')
    print('*', end='')

    mid = round(n - 2 * left_right - 2)
    if mid >= 0:
        print('-' * mid, end='')
        print('*', end='')

    print('-' * left_right, end='')
    print()

    if left_right > (n - 1) // 2 - 1:
        break
