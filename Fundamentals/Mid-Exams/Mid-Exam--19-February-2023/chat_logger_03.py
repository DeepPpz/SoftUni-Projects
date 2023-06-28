chat = []

while True:
    command = input().split()

    if command[0] == 'end':
        print(*chat, sep='\n')
        exit()

    if command[0] == 'Chat':
        chat.append(command[1])

    elif command[0] == 'Delete':
        if command[1] in chat:
            chat.remove(command[1])

    elif command[0] == 'Edit':
        if command[1] in chat:
            idx = chat.index(command[1])
            chat.insert(idx, command[2])
            chat.pop(idx + 1)

    elif command[0] == 'Pin':
        if command[1] in chat:
            chat.remove(command[1])
            chat.append(command[1])

    elif command[0] == 'Spam':
        chat.extend(command[1:])
