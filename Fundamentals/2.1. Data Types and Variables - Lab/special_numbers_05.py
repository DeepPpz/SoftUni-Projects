n = int(input())

for number in range(1, n+1):
    sum, num = 0, number
    special_flag = False

    while num >= 1:
        sum += num % 10
        num //= 10

    if sum in [5, 7, 11]:
        special_flag = True

    print(f'{number} -> {special_flag}')