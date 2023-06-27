nylon_amount = int(input())
paint_amount = int(input())
diluent_amount = int(input())
work_hours = int(input())

nylon = (nylon_amount + 2) * 1.50
paint = (paint_amount + paint_amount * 0.1) * 14.5
diluent = diluent_amount * 5

materials = nylon + paint + diluent + 0.4
work = work_hours * (materials * 0.3)
total_price = materials + work

print(total_price)
