def is_valid_index(index):
    if 0 <= index < len(targets):
        return True
    return False


targets = [int(x) for x in input().split()]

while True:
    command = input().split()
    action = command[0]

    if action == "End":
        print(*targets, sep='|')
        exit()

    if action == "Shoot":
        idx, power = map(int, (command[1], command[2]))
        if is_valid_index(idx):
            targets[idx] -= power
            if targets[idx] <= 0:
                targets.pop(idx)

    elif action == "Add":
        idx, value = map(int, (command[1], command[2]))
        if is_valid_index(idx):
            targets.insert(idx, value)
        else:
            print("Invalid placement!")

    elif action == "Strike":
        idx, radius = map(int, (command[1], command[2]))
        start_idx, end_idx = (idx - radius), (idx + radius + 1)
        if is_valid_index(idx) and is_valid_index(start_idx) and is_valid_index(end_idx):
            targets = targets[:start_idx] + targets[end_idx:]
        else:
            print("Strike missed!")
