chick_amount = int(input())
fish_amount = int(input())
vegan_amount = int(input())

chick = chick_amount * 10.35
fish = fish_amount * 12.4
vegan = vegan_amount * 8.15
menu_price = chick + fish + vegan
total_price = menu_price + menu_price * 0.2 + 2.5

print(total_price)