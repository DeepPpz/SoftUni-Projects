gifts = input().split()

while True:
    command = input().split()

    if command == ['No', 'Money']:
        break

    elif 'OutOfStock' in command:
        for i in range(len(gifts)):
            if gifts[i] == command[1]:
                gifts[i] = 'None'

    elif 'Required' in command:
        index = int(command[2])
        if 0 <= index < len(gifts) -1:
            gifts[index] = command[1]

    elif 'JustInCase' in command:
        gifts[-1] = command[1]

for g in gifts:
    if 'None' in gifts:
        gifts.remove('None')

print(*gifts, sep=' ')