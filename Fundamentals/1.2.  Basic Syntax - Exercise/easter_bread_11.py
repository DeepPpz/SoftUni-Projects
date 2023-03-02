budget = float(input())
flour_price = float(input())

eggs_price = flour_price * 0.75
milk_price = (flour_price * 1.25) / 4
loaf_price = eggs_price + flour_price + milk_price

total_loaves, colored_eggs = 0, 0

while loaf_price < budget:
    total_loaves += 1
    colored_eggs += 3
    budget -= loaf_price

    if total_loaves % 3 == 0:
        colored_eggs -= total_loaves - 2

print(f'You made {total_loaves} loaves of Easter bread! Now you have {colored_eggs} eggs and {budget:.2f}BGN left.')