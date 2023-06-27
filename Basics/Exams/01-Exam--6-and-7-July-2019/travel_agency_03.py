town = input()
package = input()
vip_discount = input()
nights_count = int(input())
valid_input = False
total_price = 0

if nights_count > 7:
    nights_count -= 1

if nights_count < 1:
    print("Days must be positive number!")
    exit(0)

elif town == "Bansko" or town == "Borovets":
    if package == "noEquipment":
        valid_input = True
        total_price = nights_count * 80
        if vip_discount == "yes":
            total_price *= 0.95
    elif package == "withEquipment":
        valid_input = True
        total_price = nights_count * 100
        if vip_discount == "yes":
            total_price *= 0.90

elif town == "Varna" or town == "Burgas":
    if package == "noBreakfast":
        valid_input = True
        total_price = nights_count * 100
        if vip_discount == "yes":
            total_price *= 0.93
    elif package == "withBreakfast":
        valid_input = True
        total_price = nights_count * 130
        if vip_discount == "yes":
            total_price *= 0.88

if valid_input:
    print(f"The price is {total_price:.2f}lv! Have a nice time!")
else:
    print("Invalid input!")
