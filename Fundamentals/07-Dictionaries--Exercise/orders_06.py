data = input().split()
inventory = {}

while data[0] != "buy":
    product = data[0]
    price = float(data[1])
    quantity = int(data[2])

    if product in inventory:
        quantity += inventory[product][1]
    inventory[product] = [price, quantity]

    data = input().split()

for (key, value) in inventory.items():
    total_price = value[0] * value[1]
    print(f"{key} -> {total_price:.2f}")
