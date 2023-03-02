pairs = int(input())

current_value = 0
past_value = 0
diff = 0
maxdiff = 0
diff_flag = False

for num in range(pairs):
    first_num = int(input())
    second_num = int(input())

    current_value = first_num + second_num

    if current_value != past_value and num != 0:
        diff_flag = True
        diff = abs(current_value - past_value)
        if diff > maxdiff: maxdiff = diff

    past_value = current_value

if diff_flag == True:
    print(f'No, maxdiff={maxdiff}')
else:
    print(f'Yes, value={current_value}')