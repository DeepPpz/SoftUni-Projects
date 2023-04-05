string_to_manipulate = input()

while True:
    command = input().split()
    action = command[0]

    if action == "End":
        exit(0)

    if action == "Translate":
        char, replacement = map(str, (command[1], command[2]))
        string_to_manipulate = string_to_manipulate.replace(char, replacement)
        print(string_to_manipulate)

    elif action == "Includes":
        substring = command[1]
        if substring in string_to_manipulate:
            print("True")
        else:
            print("False")

    elif action == "Start":
        substring = command[1]
        if string_to_manipulate.startswith(substring):
            print("True")
        else:
            print("False")

    elif action == "Lowercase":
        string_to_manipulate = string_to_manipulate.lower()
        print(string_to_manipulate)

    elif action == "FindIndex":
        char = command[1]
        for i in range(len(string_to_manipulate) - 1, -1, -1):
            if string_to_manipulate[i] == char:
                print(i)
                break

    elif action == "Remove":
        idx, count = map(int, (command[1], command[2]))
        string_to_manipulate = string_to_manipulate[:idx] + string_to_manipulate[idx +count:]
        print(string_to_manipulate)
