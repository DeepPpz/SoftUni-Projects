count = int(input())

max_num = - 10000000000000000000000000000
sum_num = 0

for i in range(count):
    num = int(input())

    if max_num < num:
        max_num = num
    sum_num += num

if max_num == sum_num - max_num:
    print('Yes')
    print(f'Sum = {sum_num - max_num}')
else:
    print('No')
    print(f'Diff = {abs(sum_num - max_num * 2)}')
