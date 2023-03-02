n = int(input())

price, total_price = 0, 0

for orders in range(n):
    price_capsule = float(input())
    days = int(input())
    capsules = int(input())

    if not 0.01 <= price_capsule <= 100 or not 1 <= days <= 31 or not 1 <= capsules <= 2000:
        continue

    price = price_capsule * days * capsules
    total_price += price
    print(f'The price for the coffee is: ${price:.2f}')

print(f'Total: ${total_price:.2f}')