number = int(input())

current_num = 1
end_flag = False

for row in range(1, number + 1):
    for column in range(1, row + 1):
        if current_num > number:
            end_flag = True
            break
        print(f'{current_num}', end=' ')
        current_num += 1
    if end_flag:
        break
    print()
