budget = float(input())
extra_count = int(input())
wear_price = float(input())

decor = budget * 0.1
sum_extra = extra_count * wear_price

if extra_count > 150:
    sum_extra -= sum_extra * 0.1

total_expenses = sum_extra + decor

if total_expenses > budget:
    print('Not enough money!')
    print(f'Wingard needs {total_expenses - budget:.2f} leva more.')
else:
    print('Action!')
    print(f'Wingard starts filming with {budget - total_expenses:.2f} leva left.')