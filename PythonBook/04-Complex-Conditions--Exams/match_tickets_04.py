budget = float(input())
category = input().lower()
people = int(input())

transport, tickets = 0, 0

if category == 'vip':
    tickets = people * 499.99
elif category == 'normal':
    tickets = people * 249.99

if 1 <= people <= 4:
    transport = budget * 0.75
elif people <= 9:
    transport = budget * 0.60
elif people <= 24:
    transport = budget * 0.50
elif people <= 49:
    transport = budget * 0.40
elif people >= 50:
    transport = budget * 0.25

diff = budget - transport - tickets

if diff >= 0:
    print(f"Yes! You have {diff:.2f} leva left.")
else:
    print(f"Not enough money! You need {abs(diff):.2f} leva.")