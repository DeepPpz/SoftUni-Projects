age = int(input())

drinks = ''

if age <= 14:
    drinks = 'toddy'
elif age <= 18:
    drinks = 'coke'
elif age <= 21:
    drinks = 'beer'
else:
    drinks = 'whisky'

print(f'drink {drinks}')