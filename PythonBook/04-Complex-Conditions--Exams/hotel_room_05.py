month = input().lower()
nights = int(input())

studio_price, apart_price = 0, 0

if month == 'may' or month == 'october':
    studio_price = nights * 50
    apart_price = nights * 65

    if nights > 14:
        studio_price *= 0.70
    elif nights > 7:
        studio_price *= 0.95

elif month == 'june' or month == 'september':
    studio_price = nights * 75.20
    apart_price = nights * 68.70

    if nights > 14:
        studio_price *= 0.80

elif month == 'july' or month == 'august':
    studio_price = nights * 76
    apart_price = nights * 77

if nights > 14:
    apart_price *= 0.90

print(f"Apartment: {apart_price:.2f} lv.")
print(f"Studio: {studio_price:.2f} lv.")