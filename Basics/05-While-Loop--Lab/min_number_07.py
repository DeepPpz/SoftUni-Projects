entry = input()
min_num = 100000000000000000000000000

while entry != 'Stop':
    number = int(entry)

    if number < min_num:
        min_num = number

    entry = input()

print(f'{min_num}')
