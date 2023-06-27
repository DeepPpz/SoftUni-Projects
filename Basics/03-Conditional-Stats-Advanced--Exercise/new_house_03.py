flowers = input()
amount = int(input())
budget = int(input())
total_price = 0

if flowers == 'Roses':
    total_price = amount * 5.00
    if amount > 80:
        total_price -= total_price * 0.1
elif flowers == 'Dahlias':
    total_price = amount * 3.80
    if amount > 90:
        total_price -= total_price * 0.15
elif flowers == 'Tulips':
    total_price = amount * 2.80
    if amount > 80:
        total_price -= total_price * 0.15
elif flowers == 'Narcissus':
    if amount < 120:
        total_price = amount * 3.00 * 1.15
    else:
        total_price = amount * 3.00
elif flowers == 'Gladiolus':
    if amount < 80:
        total_price = amount * 2.50 * 1.20
    else:
        total_price = amount * 2.50

if budget >= total_price:
    print(f'Hey, you have a great garden with {amount} {flowers} and {budget - total_price:.2f} leva left.')
else:
    print(f'Not enough money, you need {total_price - budget:.2f} leva more.')
