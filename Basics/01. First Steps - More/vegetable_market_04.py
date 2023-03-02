veg_price = float(input())
fruit_price = float(input())
veg_amount = int(input())
fruit_amount = int(input())
rate = 1.94

income_bg = veg_price * veg_amount + fruit_price * fruit_amount
income = income_bg / rate

print(f'{income:.2f}')