fruit = input()
day = input()
amount = float(input())

if day in ['Monday', 'Tuesday', 'Wednesday', 'Thursday', 'Friday']:
    if fruit == 'banana':
        print(f'{amount * 2.50:.2f}')
    elif fruit == 'apple':
        print(f'{amount * 1.20:.2f}')
    elif fruit == 'orange':
        print(f'{amount * 0.85:.2f}')
    elif fruit == 'grapefruit':
        print(f'{amount * 1.45:.2f}')
    elif fruit == 'kiwi':
        print(f'{amount * 2.70:.2f}')
    elif fruit == 'pineapple':
        print(f'{amount * 5.50:.2f}')
    elif fruit == 'grapes':
        print(f'{amount * 3.85:.2f}')
    else:
        print('error')

elif day in ['Saturday', 'Sunday']:
    if fruit == 'banana':
        print(f'{amount * 2.70:.2f}')
    elif fruit == 'apple':
        print(f'{amount * 1.25:.2f}')
    elif fruit == 'orange':
        print(f'{amount * 0.90:.2f}')
    elif fruit == 'grapefruit':
        print(f'{amount * 1.60:.2f}')
    elif fruit == 'kiwi':
        print(f'{amount * 3.00:.2f}')
    elif fruit == 'pineapple':
        print(f'{amount * 5.60:.2f}')
    elif fruit == 'grapes':
        print(f'{amount * 4.20:.2f}')
    else:
        print('error')

else:
    print('error')