season = input()
km_month = float(input())

total_salary = 0

if km_month <= 5000:
    if season in ['Spring', 'Autumn']:
        total_salary = km_month * 0.75 * 4
    elif season == 'Summer':
        total_salary = km_month * 0.90 * 4
    elif season == 'Winter':
        total_salary = km_month * 1.05 * 4

elif km_month <= 10000:
    if season in ['Spring', 'Autumn']:
        total_salary = km_month * 0.95 * 4
    elif season == 'Summer':
        total_salary = km_month * 1.10 * 4
    elif season == 'Winter':
        total_salary = km_month * 1.25 * 4

elif km_month <= 20000:
    total_salary = km_month * 1.45 * 4

total_salary -= total_salary * 0.1

print(f'{total_salary:.2f}')
