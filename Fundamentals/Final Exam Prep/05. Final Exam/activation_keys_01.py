activation_key = input()

while True:
    line = input().split(">>>")
    command = line[0]

    if command == "Generate":
        print(f"Your activation key is: {activation_key}")
        exit()

    if command == "Contains":
        substring = line[1]
        if substring in activation_key:
            print(f"{activation_key} contains {substring}")
        else:
            print(f"Substring not found!")

    elif command == "Flip":
        case = line[1].lower()
        start_idx, end_idx = int(line[2]), int(line[3])
        if case == "upper":
            activation_key = activation_key[:start_idx] + \
                             activation_key[start_idx:end_idx].upper() + activation_key[end_idx:]
        elif case == "lower":
            activation_key = activation_key[:start_idx] + \
                             activation_key[start_idx:end_idx].lower() + activation_key[end_idx:]
        print(f"{activation_key}")

    elif command == "Slice":
        start_idx, end_idx = int(line[1]), int(line[2])
        activation_key = activation_key[:start_idx] + activation_key[end_idx:]
        print(f"{activation_key}")
