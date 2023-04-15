targets = [int(x) for x in input().split()]

while True:
    idx = input()
    if idx == "End":
        print(f"Shot targets: {targets.count(-1)} -> ", end='')
        print(*targets, sep=' ')
        exit()

    idx = int(idx)
    if idx >= len(targets):
        continue
    if targets[idx] == -1:
        continue

    curr_value = targets[idx]
    targets[idx] = -1

    for i in range(len(targets)):
        if targets[i] == -1:
            continue
        elif targets[i] > curr_value:
            targets[i] -= curr_value
        elif targets[i] <= curr_value:
            targets[i] += curr_value
