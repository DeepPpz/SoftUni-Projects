n = int(input())

left_sum, right_sum = 0, 0

for i in range(0, n):
    number = int(input())
    left_sum += number

for i in range(n, n * 2):
    number = int(input())
    right_sum += number

if left_sum == right_sum:
    print(f'Yes, sum = {left_sum}')
else:
    print('No, diff = {0}'.format(abs(left_sum - right_sum)))