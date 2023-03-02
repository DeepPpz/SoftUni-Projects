count = int(input())

odd_sum = 0
even_sum = 0

for i in range(count):
    number = int(input())
    if i % 2 == 0: even_sum += number
    else: odd_sum += number

if even_sum == odd_sum:
    print('Yes')
    print(f'Sum = {even_sum}')
else:
    print('No')
    print(f'Diff = {abs(even_sum - odd_sum)}')