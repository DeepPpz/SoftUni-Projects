days = int(input())
place = input()
rating = input()

total_price = 0

if place == 'room for one person':
    total_price = (days - 1) * 18.00

elif place == 'apartment':
    total_price = (days - 1) * 25.00
    if days < 10:
        total_price -= total_price * 0.3
    elif days <= 15:
        total_price -= total_price * 0.35
    elif days > 15:
        total_price -= total_price * 0.5

elif place == 'president apartment':
    total_price = (days - 1) * 35.00
    if days < 10:
        total_price -= total_price * 0.1
    elif days <= 15:
        total_price -= total_price * 0.15
    elif days > 15:
        total_price -= total_price * 0.2

if rating == 'positive':
    total_price += total_price * 0.25
elif rating == 'negative':
    total_price -= total_price * 0.1

print(f'{total_price:.2f}')