budget = int(input())
season = input()
fishers = int(input())

total_rent = 0

if season == 'Spring':
    total_rent = 3000
    if fishers <= 6:
        total_rent -= total_rent * 0.1
    elif 7 <= fishers <= 11:
        total_rent -= total_rent * 0.15
    elif fishers >= 12:
        total_rent -= total_rent * 0.25

elif season in ['Summer', 'Autumn']:
    total_rent = 4200
    if fishers <= 6:
        total_rent -= total_rent * 0.1
    elif 7 <= fishers <= 11:
        total_rent -= total_rent * 0.15
    elif fishers >= 12:
        total_rent -= total_rent * 0.25

elif season == 'Winter':
    total_rent = 2600
    if fishers <= 6:
        total_rent -= total_rent * 0.1
    elif 7 <= fishers <= 11:
        total_rent -= total_rent * 0.15
    elif fishers >= 12:
        total_rent -= total_rent * 0.25

if fishers % 2 == 0 and season != 'Autumn':
    total_rent -= total_rent * 0.05

if budget >= total_rent:
    print(f'Yes! You have {budget - total_rent:.2f} leva left.')
else:
    print(f'Not enough money! You need {total_rent - budget:.2f} leva.')