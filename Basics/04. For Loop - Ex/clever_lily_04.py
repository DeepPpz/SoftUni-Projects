age = int(input())
wash_price = float(input())
toy_price = int(input())

total_money = 0
brother = 0

for year in range(age + 1):
    if year % 2 == 0:
        total_money += year * 5
        brother += 1
    else: total_money += toy_price

total_money -= brother - 1

if total_money >= wash_price:
    print(f'Yes! {total_money - wash_price:.2f}')
else:
    print(f'No! {wash_price - total_money:.2f}')