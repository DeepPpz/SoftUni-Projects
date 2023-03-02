budget = float(input())
season = input()

accom = str
location = str
total_price = 0

if budget <= 1000:
    accom = 'Camp'
    if season == 'Summer':
        location = 'Alaska'
        total_price = budget * 0.65
    elif season == 'Winter':
        location = 'Morocco'
        total_price = budget * 0.45

elif budget <= 3000:
    accom = 'Hut'
    if season == 'Summer':
        location = 'Alaska'
        total_price = budget * 0.80
    elif season == 'Winter':
        location = 'Morocco'
        total_price = budget * 0.60

elif budget > 3000:
    accom = 'Hotel'
    total_price = budget * 0.9
    if season == 'Summer':
        location = 'Alaska'
    elif season == 'Winter':
        location = 'Morocco'

print(f'{location} - {accom} - {total_price:.2f}')