trip_price = float(input())
puzzles_amount = int(input())
dolls_amount = int(input())
bears_amount = int(input())
minions_amount = int(input())
trucks_amount = int(input())

sum_order = puzzles_amount * 2.60
sum_order += dolls_amount * 3.00
sum_order += bears_amount * 4.10
sum_order += minions_amount * 8.20
sum_order += trucks_amount * 2.00

toys_count = puzzles_amount + dolls_amount + bears_amount + minions_amount + trucks_amount

if toys_count >= 50:
    sum_order -= sum_order * 0.25

total_money = sum_order - sum_order * 0.1

if total_money >= trip_price:
    print(f'Yes! {total_money - trip_price:.2f} lv left.')
else:
    print(f'Not enough money! {trip_price - total_money:.2f} lv needed.')