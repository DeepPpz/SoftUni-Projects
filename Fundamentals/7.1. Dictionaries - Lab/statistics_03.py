inventory = {}

while True:
    products = input().split(': ')

    if products[0] == 'statistics':
        break

    product = products[0]
    quantity = products[1]

    if product not in inventory:
        inventory[product] = int(quantity)
    else:
        inventory[product] += int(quantity)

print("Products in stock:")
[print(f"- {product}: {quantity}") for (product, quantity) in inventory.items()]
print(f"Total Products: {len(inventory)}")
print(f"Total Quantity: {sum(inventory.values())}")
