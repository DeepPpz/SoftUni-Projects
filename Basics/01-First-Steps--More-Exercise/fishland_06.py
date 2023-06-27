mackerel_price = float(input())
sprat_price = float(input())
bonito_amount = float(input())
scad_amount = float(input())
mussels_amount = int(input())

bonito_price = mackerel_price * 1.60
scad_price = sprat_price * 1.80
mussels_price = 7.50

total_price = bonito_price * bonito_amount + scad_price * scad_amount + mussels_price * mussels_amount

print(f'{total_price:.2f}')
