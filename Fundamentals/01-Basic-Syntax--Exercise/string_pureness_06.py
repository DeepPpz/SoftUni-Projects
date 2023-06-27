n = int(input())

for strings in range(n):
    pure_flag = True
    current_string = input()

    for i in range(len(current_string)):
        check = current_string[i]
        if ord(check) in [44, 46, 95]:
            pure_flag = False
            break

    if pure_flag:
        print(f'{current_string} is pure.')
    else:
        print(f'{current_string} is not pure!')
