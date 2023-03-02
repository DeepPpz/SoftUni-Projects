money = float(input())
year_to = int(input())

age = 18
years_lived = year_to - 1799

for i in range(years_lived):
    if i % 2 == 0: money -= 12000
    else: money -= 12000 + 50 * age
    age += 1

if money >= 0:
    print(f'Yes! He will live a carefree life and will have {money:.2f} dollars left.')
else:
    print(f'He will need {abs(money):.2f} dollars to survive.')