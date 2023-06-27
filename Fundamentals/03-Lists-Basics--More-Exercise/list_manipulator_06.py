int_list = [int(n) for n in input().split()]

length = len(int_list)

while True:
    command = input().split()
    odds = [num for num in int_list if num % 2 != 0]
    evens = [num for num in int_list if num % 2 == 0]

    if command[0] == 'end':
        print(int_list)
        exit()

    if command[0] == 'exchange':
        idx = int(command[1])
        if 0 <= idx < length:
            int_list = int_list[idx + 1:] + int_list[:idx + 1]
        else:
            print('Invalid index')

    elif command[0] == 'max':
        if command[1] == 'odd' and odds:
            temp_value = odds[0]
            idx = int_list.index(temp_value)
            for i in range(length):
                if (int_list[i] in odds) and (int_list[i] >= temp_value):
                    temp_value = int_list[i]
                    idx = i
            print(idx)
        elif command[1] == 'even' and evens:
            temp_value = evens[0]
            idx = int_list.index(temp_value)
            for i in range(length):
                if (int_list[i] in evens) and (int_list[i] >= temp_value):
                    temp_value = int_list[i]
                    idx = i
            print(idx)
        else:
            print('No matches')

    elif command[0] == 'min':
        if command[1] == 'odd' and odds:
            temp_value = odds[0]
            idx = int_list.index(temp_value)
            for i in range(length):
                if (int_list[i] in odds) and (int_list[i] <= temp_value):
                    temp_value = int_list[i]
                    idx = i
            print(idx)
        elif command[1] == 'even' and evens:
            temp_value = evens[0]
            idx = int_list.index(temp_value)
            for i in range(length):
                if (int_list[i] in evens) and (int_list[i] <= temp_value):
                    temp_value = int_list[i]
                    idx = i
            print(idx)
        else:
            print('No matches')

    elif command[0] == 'first':
        count = int(command[1])
        if count > length:
            print('Invalid count')
            continue

        if command[2] == 'odd':
            print(odds[:count])
        elif command[2] == 'even':
            print(evens[:count])

    elif command[0] == 'last':
        count = int(command[1])
        if count > length:
            print('Invalid count')
            continue

        if command[2] == 'odd':
            print(odds[-count:])
        elif command[2] == 'even':
            print(evens[-count:])
