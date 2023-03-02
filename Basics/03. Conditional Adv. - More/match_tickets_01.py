budget = float(input())
category = input()
people = int(input())

transport = 0
ticket_sum = 0
vip_flag = False

if category == 'Normal':
    if 1 <= people <= 4:
        transport = budget * 0.75
    elif 5 <= people <= 9:
        transport = budget * 0.6
    elif 10 <= people <= 24:
        transport = budget * 0.5
    elif 25 <= people <= 49:
        transport = budget * 0.4
    elif people >= 50:
        transport = budget * 0.25
elif category == 'VIP':
    vip_flag = True
    if 1 <= people <= 4:
        transport = budget * 0.75
    elif 5 <= people <= 9:
        transport = budget * 0.6
    elif 10 <= people <= 24:
        transport = budget * 0.5
    elif 25 <= people <= 49:
        transport = budget * 0.4
    elif people >= 50:
        transport = budget * 0.25

if vip_flag:
    ticket_sum = people * 499.99
    total_price = transport + ticket_sum
    if budget > total_price:
        print(f'Yes! You have {budget - total_price:.2f} leva left.')
    else:
        print(f'Not enough money! You need {total_price - budget:.2f} leva.')
else:
    ticket_sum = people * 249.99
    total_price = transport + ticket_sum
    if budget > total_price:
        print(f'Yes! You have {budget - total_price:.2f} leva left.')
    else:
        print(f'Not enough money! You need {total_price - budget:.2f} leva.')