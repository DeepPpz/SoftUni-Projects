n = int(input()) #days
m = float(input()) #salary/day
rate = float(input()) # 1 dol = X lv

bonus = n * m * 2.5
total_salary = n * m * 12 + bonus
total_salary *= 0.75
total_salary /= 365
total_salary *= rate

print(f'{total_salary:.2f}')