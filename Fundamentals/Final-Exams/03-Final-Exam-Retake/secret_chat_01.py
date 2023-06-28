message = input()

while True:
    line = input().split(":|:")
    command = line[0]

    if command == "Reveal":
        print(f"You have a new text message: {message}")
        exit(0)

    if command == "InsertSpace":
        idx = int(line[1])
        message = message[:idx] + " " + message[idx:]
        print(message)

    elif command == "Reverse":
        substring = line[1]
        if substring not in message:
            print("error")
        else:
            message = message.replace(substring, "", 1)
            substring = substring[::-1]
            message = message + substring
            print(message)

    elif command == "ChangeAll":
        substring, replacement = line[1], line[2]
        message = message.replace(substring, replacement)
        print(message)
