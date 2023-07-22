age = int(input())
washing_machine = float(input())
toy_price = int(input())
money, toys = 0, 0

for i in range(1, age + 1):
    if i % 2 == 0:
        money += i * 5
        money -= 1
    else:
        toys += 1

money += toys * toy_price
diff = abs(money - washing_machine)

if money >= washing_machine:
    print(f"Yes! {diff:.2f}")
else:
    print(f"No! {diff:.2f}")
