type = input()
litres = float(input())

if type == 'Diesel':
    if litres >= 25:
        print(f'You have enough {type.lower()}.')
    else:
        print(f'Fill your tank with {type.lower()}!')
elif type == 'Gasoline':
    if litres >= 25:
        print(f'You have enough {type.lower()}.')
    else:
        print(f'Fill your tank with {type.lower()}!')
elif type == 'Gas':
    if litres >= 25:
        print(f'You have enough {type.lower()}.')
    else:
        print(f'Fill your tank with {type.lower()}!')
else:
    print('Invalid fuel!')