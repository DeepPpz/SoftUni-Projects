pens_count = int(input())
markers_count = int(input())
detergent_l = int(input())
discount_perc = int(input())

pens = pens_count * 5.8
markers = markers_count * 7.20
detergent = detergent_l * 1.20
price = pens + markers + detergent
total_price = price - (price * (discount_perc/100))

print(total_price)