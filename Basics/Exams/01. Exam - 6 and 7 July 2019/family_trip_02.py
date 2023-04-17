budget = float(input())
total_stays = int(input())
price_per_night = float(input())
extra_expenses = int(input()) / 100

if total_stays > 7:
    price_per_night *= 0.95

extra_expenses = extra_expenses * budget
total_expenses = total_stays * price_per_night + extra_expenses
diff = abs(budget - total_expenses)

if budget >= total_expenses:
    print(f"Ivanovi will be left with {diff:.2f} leva after vacation.")
else:
    print(f"{diff:.2f} leva needed.")
