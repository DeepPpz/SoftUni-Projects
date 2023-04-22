budget = float(input())
extras = int(input())
clothes_per_person = float(input())

decors = budget * 0.10
clothes = clothes_per_person * extras

if extras > 150:
    clothes *= 0.90

total_expenses = decors + clothes

diff = budget - total_expenses

if diff >= 0:
    print(f"Action!\nWingard starts filming with {diff:.2f} leva left.")
else:
    print(f"Not enough money!\nWingard needs {abs(diff):.2f} leva more.")
