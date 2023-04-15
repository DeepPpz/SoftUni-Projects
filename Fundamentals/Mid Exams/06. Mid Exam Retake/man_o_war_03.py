pirate_ship = [int(x) for x in input().split('>')]
warship = [int(y) for y in input().split('>')]
max_health = int(input())

while True:
    command = input().split()

    if command[0] == 'Retire':
        print(f'Pirate ship status: {sum(pirate_ship)}')
        print(f'Warship status: {sum(warship)}')
        exit()

    if command[0] == 'Fire':
        idx, dmg = map(int, (command[1], command[2]))
        if idx < 0 or idx >= len(warship):
            continue
        warship[idx] -= dmg
        if warship[idx] <= 0:
            print('You won! The enemy ship has sunken.')
            exit()

    elif command[0] == 'Defend':
        start_idx, end_idx, dmg = map(int, (command[1], command[2], command[3]))
        if start_idx < 0 or start_idx >= len(pirate_ship) or end_idx < 0 or end_idx >= len(pirate_ship):
            continue
        for i in range(start_idx, end_idx +1):
            pirate_ship[i] -= dmg
            if pirate_ship[i] <= 0:
                print('You lost! The pirate ship has sunken.')
                exit()

    elif command[0] == 'Repair':
        idx, health = map(int, (command[1], command[2]))
        if idx < 0 or idx >= len(pirate_ship):
            continue
        pirate_ship[idx] = min(max_health, health + pirate_ship[idx])

    elif command[0] == 'Status':
        counter = 0
        for sect in pirate_ship:
            if sect / max_health < 0.2:
                counter += 1
        if counter != 0:
            print(f'{counter} sections need repair.')