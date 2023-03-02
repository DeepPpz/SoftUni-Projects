n = int(input())

total_sum = 0
max_num = -10000000000000000000000

for i in range(n):
    num = int(input())

    total_sum += num
    if num > max_num:
        max_num = num

total_sum -= max_num

if total_sum == max_num:
    print('Yes')
    print(f'Sum = {total_sum}')
else:
    print('No')
    print(f'Diff = ', abs(total_sum - max_num))