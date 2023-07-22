inherited_money = float(input())
year_to_live = int(input())
years_old = 18
money_needed = 0

for i in range(1800, year_to_live + 1):
    if i % 2 != 0:
        money_needed += 50 * years_old

    money_needed += 12000
    years_old += 1

diff = abs(money_needed - inherited_money)

if money_needed <= inherited_money:
    print(f"Yes! He will live a carefree life and will have {diff:.2f} dollars left.")
else:
    print(f"He will need {diff:.2f} dollars to survive.")
