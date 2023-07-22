city = input().lower()
sales = float(input())

comission = 0
error_flag = False

if sales < 0 or city not in ['sofia', 'varna', 'plovdiv']:
    error_flag = True
elif 0 <= sales <= 500:
    if city == 'sofia':
        comission = sales * 0.05
    elif city == 'varna':
        comission = sales * 0.045
    elif city == 'plovdiv':
        comission = sales * 0.055

elif 500 < sales <= 1000:
    if city == 'sofia':
        comission = sales * 0.07
    elif city == 'varna':
        comission = sales * 0.075
    elif city == 'plovdiv':
        comission = sales * 0.08

elif 1000 < sales <= 10000:
    if city == 'sofia':
        comission = sales * 0.08
    elif city == 'varna':
        comission = sales * 0.10
    elif city == 'plovdiv':
        comission = sales * 0.12

elif sales > 10000:
    if city == 'sofia':
        comission = sales * 0.12
    elif city == 'varna':
        comission = sales * 0.13
    elif city == 'plovdiv':
        comission = sales * 0.145

if error_flag:
    print('error')
else:
    print(f'{comission:.2f}')