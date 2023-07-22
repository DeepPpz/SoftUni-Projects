n = int(input())

prev_sum, curr_sum = 0, 0
curr_diff, max_diff = 0, 0

for i in range(n):
    n1 = int(input())
    n2 = int(input())

    curr_sum = n1 + n2

    if prev_sum != curr_sum and i != 0:
        curr_diff = abs(curr_sum - prev_sum)

        if max_diff < curr_diff:
            max_diff = curr_diff

    prev_sum = curr_sum

if max_diff != 0:
    print(f'No, maxdiff={max_diff}')
else:
    print(f'Yes, value={curr_sum}')