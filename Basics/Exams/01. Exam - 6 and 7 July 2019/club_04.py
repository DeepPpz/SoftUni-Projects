target_profit = float(input())
total_profit = 0
cocktail = input()

while cocktail != "Party!":
    cocktail_price = len(cocktail)
    cocktail_count = int(input())

    order_price = cocktail_price * cocktail_count
    if order_price % 2 != 0:
        order_price *= 0.75

    total_profit += order_price
    if target_profit <= total_profit:
        break

    cocktail = input()

diff = target_profit - total_profit

if diff > 0:
    print(f"We need {diff:.2f} leva more.")
else:
    print("Target acquired.")
print(f"Club income - {total_profit:.2f} leva.")
