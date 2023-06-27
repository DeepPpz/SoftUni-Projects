year_tax = int(input())

shoes = year_tax - year_tax * 0.4
suit = shoes - shoes * 0.2
ball = suit / 4
accessories = ball / 5
total_expenses = year_tax + shoes + suit + ball + accessories

print(total_expenses)
