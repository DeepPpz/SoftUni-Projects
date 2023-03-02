budget = float(input())
season = input()

destination, place, expenses = '', '', 0

if budget <= 100:
    destination = 'Bulgaria'
    if season == 'summer':
        place = 'Camp'
        expenses = budget * 0.30
    elif season == 'winter':
        place = 'Hotel'
        expenses = budget * 0.70

elif budget <= 1000:
    destination = 'Balkans'
    if season == 'summer':
        place = 'Camp'
        expenses = budget * 0.40
    elif season == 'winter':
        place = 'Hotel'
        expenses = budget * 0.80

else:
    destination = 'Europe'
    place = 'Hotel'
    expenses = budget * 0.90

print(f"Somewhere in {destination}")
print(f"{place} - {expenses:.2f}")