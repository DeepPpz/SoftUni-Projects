treasure_chest = [x for x in input().split('|')]

while True:
    command = input().split()

    if command[0] == 'Yohoho!':
        break

    if command[0] == 'Loot':
        new_loots = command[1:]
        for item in new_loots:
            if item not in treasure_chest:
                treasure_chest.insert(0, item)

    elif command[0] == 'Drop':
        idx = int(command[1])

        if 0 <= idx < len(treasure_chest) -1:
            treasure_chest.append(treasure_chest[idx])
            treasure_chest.pop(idx)

    elif command[0] == 'Steal':
        count = int(command[1])
        stolen_items = treasure_chest[-count:]
        print(*stolen_items, sep=', ')
        del treasure_chest[-count:]

if not treasure_chest:
    print('Failed treasure hunt.')
else:
    avg_treasure_gain = sum(len(x) for x in treasure_chest) / len(treasure_chest)
    print(f'Average treasure gain: {avg_treasure_gain:.2f} pirate credits.')