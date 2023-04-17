import math

people = int(input())
entry_tax = float(input())
lounge_price = float(input())
umbrella_price = float(input())

tax_total = entry_tax * people
lounges_total = lounge_price * math.ceil(people * 0.75)
umbrellas_total = umbrella_price * math.ceil(people * 0.5)
total_price = tax_total + lounges_total + umbrellas_total

print(f"{total_price:.2f} lv.")
