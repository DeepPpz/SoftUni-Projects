entry = input()

max_num = -100000000000000000000000000

while entry != 'Stop':
    number = int(entry)

    if number > max_num:
        max_num = number

    entry = input()

print(f'{max_num}')