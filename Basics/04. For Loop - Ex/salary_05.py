tabs = int(input())
salary = float(input())

total_fines = 0

for fines in range(tabs):
    tab_name = input()
    if tab_name == 'Facebook': total_fines += 150
    elif tab_name == 'Instagram': total_fines += 100
    elif tab_name == 'Reddit': total_fines += 50

if salary <= total_fines:
    print('You have lost your salary.')
else:
    print(f'{salary - total_fines:.0f}')