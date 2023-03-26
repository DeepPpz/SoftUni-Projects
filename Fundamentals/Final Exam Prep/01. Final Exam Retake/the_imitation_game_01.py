message = input()

while True:
    command = input().split("|")
    action = command[0]

    if action == "Decode":
        print(f"The decrypted message is: {message}")
        exit()

    if action == "Move":
        num = int(command[1])
        message = message[num:] + message[:num]

    elif action == "Insert":
        idx, value = int(command[1]), command[2]
        message = message[:idx] + value + message[idx:]

    elif action == "ChangeAll":
        substring, replacement = command[1], command[2]
        message = message.replace(substring, replacement)
