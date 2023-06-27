fuel_type = input().lower()
litres = float(input())

if fuel_type == 'diesel':
    if litres >= 25:
        print(f'You have enough {fuel_type}.')
    else:
        print(f'Fill your tank with {fuel_type}!')
elif fuel_type == 'gasoline':
    if litres >= 25:
        print(f'You have enough {fuel_type}.')
    else:
        print(f'Fill your tank with {fuel_type}!')
elif fuel_type == 'gas':
    if litres >= 25:
        print(f'You have enough {fuel_type}.')
    else:
        print(f'Fill your tank with {fuel_type}!')
else:
    print('Invalid fuel!')
