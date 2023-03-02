numbers = [int(el) for el in input().split()]

while True:
    command = input().split()

    if command[0] == 'end':
        print(*numbers, sep=', ')
        exit()

    if command[0] == 'swap':
        idx_one, idx_two = map(int, (command[1], command[2]))
        numbers[idx_one], numbers[idx_two] = numbers[idx_two], numbers[idx_one]

    elif command[0] == 'multiply':
        idx_one, idx_two = map(int, (command[1], command[2]))
        numbers[idx_one] = numbers[idx_one] * numbers[idx_two]

    elif command[0] == 'decrease':
        numbers = [n - 1 for n in numbers]
