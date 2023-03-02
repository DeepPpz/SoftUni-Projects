events = input().split('|')

energy, coins = 100, 100

for i in range(len(events)):
    curr_event = events[i].split('-')
    amount = int(curr_event[1])

    if curr_event[0] == 'rest':
        if energy + amount > 100:
            amount = 100 - energy
            energy = 100
        else:
            energy += amount
        print(f'You gained {amount} energy.')
        print(f'Current energy: {energy}.')

    elif curr_event[0] == 'order':
        if energy >= 30:
            energy -= 30
            coins += amount
            print(f'You earned {amount} coins.')
        else:
            energy += 50
            print(f'You had to rest!')

    else:
        if coins >= amount:
            coins -= amount
            print(f'You bought {curr_event[0]}.')
        else:
            print(f'Closed! Cannot afford {curr_event[0]}.')
            exit()

print('Day completed!')
print(f'Coins: {coins}')
print(f'Energy: {energy}')