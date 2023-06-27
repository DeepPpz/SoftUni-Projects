import math

magnolia = int(input())
hyacinth = int(input())
rose = int(input())
cactus = int(input())
gift_price = float(input())

total_income = magnolia * 3.25
total_income += hyacinth * 4
total_income += rose * 3.5
total_income += cactus * 8
total_income -= total_income * 0.05

if total_income >= gift_price:
    print(f'She is left with {math.floor(total_income - gift_price)} leva.')
else:
    print(f'She will have to borrow {math.ceil(gift_price - total_income)} leva.')
