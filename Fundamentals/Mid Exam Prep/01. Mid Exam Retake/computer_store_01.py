net_price = 0

while True:
    price = input()

    if price == "special" or price == "regular":
        taxes = net_price * 0.20
        break

    price = float(price)
    if price >= 0:
        net_price += price
    else:
        print("Invalid price!")

if net_price == 0:
    print("Invalid order!")
else:
    print("Congratulations you've just bought a new computer!")
    print(f"Price without taxes: {net_price:.2f}$")
    print(f"Taxes: {taxes:.2f}$")
    print("-----------")
    if price == "special":
        print(f"Total price: {(net_price + taxes) * 0.90:.2f}$")
    else:
        print(f"Total price: {net_price + taxes:.2f}$")
