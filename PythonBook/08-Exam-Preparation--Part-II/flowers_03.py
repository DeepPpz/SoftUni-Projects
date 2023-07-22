chrysanthemums = int(input())
roses = int(input())
tulips = int(input())
season = input().lower()
is_holiday = input().lower()
total_price = 0

if season == "spring" or season == "summer":
    total_price += chrysanthemums * 2.00 + roses * 4.10 + tulips * 2.50
    if is_holiday == "y":
        total_price *= 1.15
    if season == "spring" and tulips > 7:
        total_price *= 0.95

elif season == "autumn" or season == "winter":
    total_price += chrysanthemums * 3.75 + roses * 4.50 + tulips * 4.15
    if is_holiday == "y":
        total_price *= 1.15
    if season == "winter" and roses >= 10:
        total_price *= 0.90

if (chrysanthemums + roses + tulips) > 20:
    total_price *= 0.80
total_price += 2

print(f"{total_price:.2f}")
