budget = float(input())
season = input()

accommodation = str
location = str
total_price = 0

if budget <= 1000:
    accommodation = 'Camp'
    if season == 'Summer':
        location = 'Alaska'
        total_price = budget * 0.65
    elif season == 'Winter':
        location = 'Morocco'
        total_price = budget * 0.45

elif budget <= 3000:
    accommodation = 'Hut'
    if season == 'Summer':
        location = 'Alaska'
        total_price = budget * 0.80
    elif season == 'Winter':
        location = 'Morocco'
        total_price = budget * 0.60

elif budget > 3000:
    accommodation = 'Hotel'
    total_price = budget * 0.9
    if season == 'Summer':
        location = 'Alaska'
    elif season == 'Winter':
        location = 'Morocco'

print(f'{location} - {accommodation} - {total_price:.2f}')
