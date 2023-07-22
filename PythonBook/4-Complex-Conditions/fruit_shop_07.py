fruit = input()
day = input()
quantity = float(input())

work_days = ['Monday', 'Tuesday', 'Wednesday', 'Thursday', 'Friday']
off_days = ['Saturday', 'Sunday']
total_price = 0
error_flag = False

if day not in work_days and day not in off_days:
    error_flag = True

if fruit == 'banana':
    if day in work_days:
        total_price = quantity * 2.50
    elif day in off_days:
        total_price = quantity * 2.70

elif fruit == 'apple':
    if day in work_days:
        total_price = quantity * 1.20
    elif day in off_days:
        total_price = quantity * 1.25

elif fruit == 'orange':
    if day in work_days:
        total_price = quantity * 0.85
    elif day in off_days:
        total_price = quantity * 0.90

elif fruit == 'grapefruit':
    if day in work_days:
        total_price = quantity * 1.45
    elif day in off_days:
        total_price = quantity * 1.60

elif fruit == 'kiwi':
    if day in work_days:
        total_price = quantity * 2.70
    elif day in off_days:
        total_price = quantity * 3.00

elif fruit == 'pineapple':
    if day in work_days:
        total_price = quantity * 5.50
    elif day in off_days:
        total_price = quantity * 5.60

elif fruit == 'grapes':
    if day in work_days:
        total_price = quantity * 3.85
    elif day in off_days:
        total_price = quantity * 4.20

else:
    error_flag = True

if error_flag:
    print('error')
else:
    print(f'{total_price:.2f}')