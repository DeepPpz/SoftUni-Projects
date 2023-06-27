product = input()
city = input()
amount = float(input())

price = 0

if city == 'Sofia':
    if product == 'coffee':
        price = amount * 0.50
    elif product == 'water':
        price = amount * 0.80
    elif product == 'beer':
        price = amount * 1.20
    elif product == 'sweets':
        price = amount * 1.45
    elif product == 'peanuts':
        price = amount * 1.60

elif city == 'Plovdiv':
    if product == 'coffee':
        price = amount * 0.40
    elif product == 'water':
        price = amount * 0.70
    elif product == 'beer':
        price = amount * 1.15
    elif product == 'sweets':
        price = amount * 1.30
    elif product == 'peanuts':
        price = amount * 1.50

elif city == 'Varna':
    if product == 'coffee':
        price = amount * 0.45
    elif product == 'water':
        price = amount * 0.70
    elif product == 'beer':
        price = amount * 1.10
    elif product == 'sweets':
        price = amount * 1.35
    elif product == 'peanuts':
        price = amount * 1.55

print(price)
