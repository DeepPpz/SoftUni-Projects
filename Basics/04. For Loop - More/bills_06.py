months = int(input())

electricity = 0
water = 0
internet = 0
others = 0
total = 0
average = 0

for bills in range(months):
    electr_bill = float(input())

    electricity += electr_bill
    water += 20
    internet += 15
    others += (electr_bill + 20 + 15) * 1.20

total = electricity + water + internet + others
average = total / months

print(f'Electricity: {electricity:.2f} lv')
print(f'Water: {water:.2f} lv')
print(f'Internet: {internet:.2f} lv')
print(f'Other: {others:.2f} lv')
print(f'Average: {average:.2f} lv')