count = int(input())

count = count * 2
left_sum = 0
right_sum = 0

for i in range(count):
    number = int(input())

    if i < count / 2:
        left_sum += number
    else:
        right_sum += number

if left_sum == right_sum:
    print(f'Yes, sum = {left_sum}')
else:
    print(f'No, diff = {abs(left_sum - right_sum)}')
