n = int(input())

for number in range(1, n + 1):
    total_sum, num = 0, number
    special_flag = False

    while num >= 1:
        total_sum += num % 10
        num //= 10

    if total_sum in [5, 7, 11]:
        special_flag = True

    print(f'{number} -> {special_flag}')
