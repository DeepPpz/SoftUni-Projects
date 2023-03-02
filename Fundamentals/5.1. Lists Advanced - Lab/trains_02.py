num_wagons = int(input())

train = [0 for i in range(num_wagons)]

while True:
    command = input().split()

    if command[0] == 'End':
        print(train)
        exit()

    if command[0] == 'add':
        train[-1] += int(command[1])

    elif command[0] == 'insert':
        idx = int(command[1])
        train[idx] += int(command[2])

    elif command[0] == 'leave':
        idx = int(command[1])
        train[idx] -= int(command[2])