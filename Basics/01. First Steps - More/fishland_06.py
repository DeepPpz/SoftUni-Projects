skum_price = float(input())
caca_price = float(input())
pala_amount = float(input())
saf_amount = float(input())
midi_amount = int(input())

pala_price = skum_price + skum_price * 0.6
saf_price = caca_price + caca_price * 0.8
midi_price = 7.5

total_price = pala_price * pala_amount + saf_price * saf_amount + midi_price * midi_amount

print(f'{total_price:.2f}')