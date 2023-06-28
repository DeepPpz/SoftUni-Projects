password = input()

while True:
    line = input().split()
    command = line[0]

    if command == "Done":
        print(f"Your password is: {password}")
        exit(0)

    if command == "TakeOdd":
        new_pass = ""
        for i in range(len(password)):
            if i % 2 != 0:
                new_pass += password[i]
        password = new_pass
        print(password)

    elif command == "Cut":
        idx, length = map(int, (line[1], line[2]))
        password = password[:idx] + password[idx + length:]
        print(password)

    elif command == "Substitute":
        substring, substitute = map(str, (line[1], line[2]))
        if substring in password:
            password = password.replace(substring, substitute)
            print(password)
        else:
            print("Nothing to replace!")
