trigger = input()

balance = 0

while trigger != 'NoMoreMoney':
    amount = float(trigger)

    if amount < 0:
        print('Invalid operation!')
        break

    print(f'Increase: {amount:.2f}')
    balance += amount

    trigger = input()

print(f'Total: {balance:.2f}')
