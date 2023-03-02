budget = float(input())
season = input()

total_spent = 0
destination = str
place = str

if budget <= 100:
    destination = 'Bulgaria'
    if season == 'summer':
        total_spent = budget * 0.3
        place = 'Camp'
    elif season == 'winter':
        total_spent = budget * 0.7
        place = 'Hotel'

elif budget <= 1000:
    destination = 'Balkans'
    if season == 'summer':
        total_spent = budget * 0.4
        place = 'Camp'
    elif season == 'winter':
        total_spent = budget * 0.8
        place = 'Hotel'

elif budget > 1000:
    destination = 'Europe'
    total_spent = budget * 0.9
    place = 'Hotel'

print(f'Somewhere in {destination}')
print(f'{place} - {total_spent:.2f}')