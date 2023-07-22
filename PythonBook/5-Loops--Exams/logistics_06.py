n = int(input())
total_price, total_tonnage = 0, 0
bus, truck, train = 0, 0, 0

for i in range(n):
    tonnage = int(input())
    total_tonnage += tonnage

    if tonnage <= 3:
        bus += tonnage
        total_price += tonnage * 200
    elif tonnage <= 11:
        truck += tonnage
        total_price += tonnage * 175
    else:
        train += tonnage
        total_price += tonnage * 120

print(f"{(total_price / total_tonnage):.2f}")
print(f"{(bus / total_tonnage * 100):.2f}%")
print(f"{(truck / total_tonnage * 100):.2f}%")
print(f"{(train / total_tonnage * 100):.2f}%")
